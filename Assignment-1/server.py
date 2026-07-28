import json
import logging
from os import environ as env
from urllib.parse import urlparse
from datetime import datetime, timezone

from auth0_server_python.auth_server.server_client import ServerClient
from auth0_server_python.auth_types import (
    LogoutOptions,
    StartInteractiveLoginOptions,
    StateData,
    TransactionData,
)
from auth0_server_python.store.abstract import AbstractDataStore
from dotenv import load_dotenv
from flask import Flask, after_this_request, redirect, request, session
from markupsafe import escape

load_dotenv()

app = Flask(__name__)
app.secret_key = env.get("AUTH0_SECRET")

logging.basicConfig(level=logging.INFO)
app.logger.setLevel(logging.INFO)
app.logger.propagate = True


class CookieStore(AbstractDataStore):
    def __init__(self, secret, cookie_name, max_age, model):
        super().__init__({"secret": secret})
        self.cookie_name = cookie_name
        self.max_age = max_age
        self.model = model

    async def set(self, identifier, state, **_):
        @after_this_request
        def apply(response):
            data = state.model_dump() if hasattr(state, "model_dump") else state
            response.set_cookie(
                self.cookie_name,
                self.encrypt(identifier, data),
                httponly=True,
                samesite="Lax",
                secure=False,
                max_age=self.max_age,
            )
            return response

    async def get(self, identifier, options=None):
        try:
            encrypted = options["request"].cookies.get(self.cookie_name)
            return (
                self.model.model_validate(
                    self.decrypt(identifier, encrypted)
                )
                if encrypted
                else None
            )
        except Exception:
            return None

    async def delete(self, *_, **__):
        @after_this_request
        def apply(response):
            response.delete_cookie(self.cookie_name)
            return response


def auth0():
    session_secret = env.get("AUTH0_SECRET")

    return ServerClient(
        domain=env.get("AUTH0_DOMAIN"),
        client_id=env.get("AUTH0_CLIENT_ID"),
        client_secret=env.get("AUTH0_CLIENT_SECRET"),
        redirect_uri=env.get("APP_BASE_URL") + "/callback",
        authorization_params={"scope": "openid profile email"},
        secret=session_secret,
        state_store=CookieStore(
            session_secret,
            "_a0_session",
            259200,
            StateData,
        ),
        transaction_store=CookieStore(
            session_secret,
            "_a0_tx",
            300,
            TransactionData,
        ),
    )


@app.route("/")
async def home():

    user = await auth0().get_user({"request": request})

    if user:

        if not session.get("login_logged"):

            app.logger.info(
                json.dumps(
                 {
                      "event": "protected_access",
                      "user_id": user.get("sub"),
                      "email": user.get("email"),
                      "route": "/protected",
                      "timestamp": datetime.now(timezone.utc).isoformat()
                 }
                         )
            )

            session["login_logged"] = True

        return f"""
                <pre>
                +------------------------------------------------------------+
                |                  AUTHENTICATION GATEWAY                    |
                +------------------------------------------------------------+

                 STATUS   : AUTHENTICATED
                 USER     : {escape(user.get("email", ""))}
                 PROVIDER : AUTH0
                 HOST     : AZURE APP SERVICE

                --------------------------------------------------------------

                [1] <a href="/protected">Protected Page</a>
                [2] <a href="/logout">Logout</a>

                --------------------------------------------------------------

                 Session established successfully.

                </pre>
            """

    return """
    <!DOCTYPE html>
    <html>
    <head>
    <title>Authentication Gateway</title>
    <style>
    body{
        background:#000;
        color:#00FF41;
        font-family:Consolas, "Courier New", monospace;
        margin:40px;
    }

    a{
        color:#00FFFF;
        text-decoration:none;
    }

    a:hover{
        text-decoration:underline;
    }

    hr{
        border:0;
        border-top:1px solid #00FF41;
    }

    .status{
        color:#FFFF66;
    }

    .title{
        color:#FFFFFF;
    }

    body{
    background:#000;
    color:#00FF41;
    font-family:Consolas, "Courier New", monospace;
    }

    .blink{
        animation: blink 1s steps(2, start) infinite;
    }

    @keyframes blink{
        50%{
            opacity:0;
        }
    }

    </style>
    </head>
    <body>
    <h1 class="title">Authentication Gateway</h1>
    <hr>
    <pre>
    Microsoft Azure Authentication Service
    System............. Online
    Identity Provider.. Auth0
    Application........ Flask
    Logging............ Enabled
    Monitoring......... Azure Monitor
    Status............. <span class="status">Waiting for authentication</span><span class="blink">█</span>
    </pre>
    <hr><p>
    > <a href="/login">Initialize Secure Session</a>
    </p>
    </body>
    </html>
"""


@app.route("/protected")
async def protected():

    user = await auth0().get_user({"request": request})

    if not user:

        app.logger.warning(
            json.dumps(
              {
                  "event": "unauthorized_access",
                  "route": "/protected",
                  "timestamp": datetime.now(timezone.utc).isoformat()
              }
            )
        )

        return redirect("/login")

    app.logger.info(json.dumps(
        {
            "event": "protected_access",
            "user_id": user.get("sub"),
            "email": user.get("email"),
            "route": "/protected",
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
    )
    )

    return f"""
        <pre>
        +------------------------------------------------------------+
        |                    PROTECTED RESOURCE                      |
        +------------------------------------------------------------+

         STATUS   : ACCESS GRANTED
         USER     : {escape(user.get("email", ""))}
         RESOURCE : /protected
         SESSION  : ACTIVE

        --------------------------------------------------------------

        [1] <a href="/">Home</a>
        [2] <a href="/logout">Logout</a>

        --------------------------------------------------------------

         Protected resource accessed successfully.

        </pre>
    """


@app.route("/login")
async def login():
    url = await auth0().start_interactive_login(
        options=StartInteractiveLoginOptions(
            authorization_params=dict(request.args),
        ),
        store_options={"request": request},
    )
    return redirect(url)


@app.route("/callback")
async def callback():
    await auth0().complete_interactive_login(
        url=request.url,
        store_options={"request": request},
    )
    return redirect("/")


@app.route("/logout")
async def logout():

    session.clear()

    url = await auth0().logout(
        options=LogoutOptions(
            return_to=env.get("APP_BASE_URL")
        ),
        store_options={"request": request},
    )

    return redirect(url)


if __name__ == "__main__":
    url = urlparse(env.get("APP_BASE_URL"))

    app.run(
        host=url.hostname,
        port=url.port or 5000,
        debug=True,
    )