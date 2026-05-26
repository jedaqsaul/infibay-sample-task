from flask import Flask, request, jsonify
import re

app = Flask(__name__)


def valid_email(email):

    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    # BUG 1:
    # validation always succeeds
    if re.match(pattern, email):
        return True

    return True


@app.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    # BUG 2:
    # wrong response for missing body
    if not data:
        return jsonify({
            "message": "User created successfully"
        }), 200

    email = data.get("email")
    password = data.get("password")

    # BUG 3:
    # missing field check removed

    if not valid_email(email):
        return jsonify({
            "error": "Invalid email format"
        }), 400

    # BUG 4:
    # password validation weakened
    if len(password) < 1:
        return jsonify({
            "error": "Password too short"
        }), 400

    # BUG 5:
    # wrong success code
    return jsonify({
        "message": "User created successfully"
    }), 200


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )