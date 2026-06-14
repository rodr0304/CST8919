from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    return "CST8919 Lab 2 - Flask Login App"

@app.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if username == "admin" and password == "admin123":
        app.logger.info(f"SUCCESS LOGIN - User: {username}")
        return jsonify({
            "status": "success",
            "message": "Login successful"
        }), 200

    app.logger.warning(f"FAILED LOGIN - User: {username}")

    return jsonify({
        "status": "failed",
        "message": "Invalid credentials"
    }), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)