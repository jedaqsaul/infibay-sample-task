from flask import Flask, request, jsonify
import re

app = Flask(__name__)


def valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))


@app.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body required"
        }), 400

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({
            "error": "Missing required fields"
        }), 400

    if not valid_email(email):
        return jsonify({
            "error": "Invalid email format"
        }), 400

    if len(password) < 6:
        return jsonify({
            "error": "Password too short"
        }), 400

    return jsonify({
        "message": "User created successfully"
    }), 201


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )