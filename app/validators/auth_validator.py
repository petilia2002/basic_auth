from functools import wraps
from flask import request, jsonify
import re


def validate_credentials(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        data = request.get_json()

        # Проверка наличия полей
        if not data or "name" not in data or "password" not in data:
            return jsonify({"error": "Username and password are required"}), 400

        username = data["name"].strip()
        password = data["password"].strip()

        # Валидация имени пользователя
        if len(username) < 3:
            return jsonify({"error": "Username must be at least 3 characters"}), 400
        if len(username) > 10:
            return jsonify({"error": "Username too long (max 10 chars)"}), 400
        if not re.match(r"^[a-zA-Z0-9_]+$", username):
            return (
                jsonify(
                    {
                        "error": "Username can only contain letters, numbers and underscores"
                    }
                ),
                400,
            )

        # Валидация пароля
        if len(password) < 4:
            return jsonify({"error": "Password must be at least 4 characters"}), 400
        if len(password) > 10:
            return jsonify({"error": "Password too long (max 10 chars)"}), 400
        if " " in password:
            return jsonify({"error": "Password cannot contain spaces"}), 400

        return f(*args, **kwargs)

    return decorated_function
