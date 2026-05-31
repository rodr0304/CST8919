import json
from os import environ as env
from urllib.parse import urlparse

from auth0_server_python.auth_server.server_client import ServerClient
from auth0_server_python.auth_types import (
    LogoutOptions,
    StartInteractiveLoginOptions,
    StateData,
    TransactionData,
)
from auth0_server_python.store.abstract import AbstractDataStore
from dotenv import load_dotenv
from flask import Flask, after_this_request, redirect, request
from markupsafe import escape

load_dotenv()

app = Flask(__name__)


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
        return f"""
        <h1>Welcome</h1>
        <p>Logged in as {escape(user.get("email", ""))}</p>
        <p><a href="/protected">Protected Page</a></p>
        <p><a href="/logout">Logout</a></p>
        """

    return """
    <h1>Flask Auth0 Lab</h1>
    <a href="/login">Login</a>
    """


@app.route("/protected")
async def protected():

    user = await auth0().get_user({"request": request})

    if not user:
        return redirect("/login")

    return f"""
    <h1>Protected Page</h1>
    <p>You are authenticated.</p>
    <p>User: {escape(user.get("email", ""))}</p>
    <a href="/">Home</a>
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