from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app.utils.request_parser import parse_request
from app.db.models import db, User, Role, UserRole
from app.utils.token_generator import generate_access_token


class AuthController:
    @staticmethod
    def registration():
        try:
            req = parse_request()
            user_data = req.body
            username, password = user_data.get("name"), user_data.get("password")

            candidate = User.query.filter_by(name=username).first()
            if candidate:
                return jsonify({"Message": "A user with that name already exists"}), 400

            password_hash = generate_password_hash(password, method="pbkdf2:sha256")
            user_data["password"] = password_hash

            user = User(**user_data)
            db.session.add(user)
            db.session.flush()

            role = Role.query.filter_by(name="user").first()
            user_role = UserRole(user_id=user.id, role_id=role.id)
            db.session.add(user_role)

            db.session.commit()
            return (
                jsonify({"Message": "The user has been successfully registered"}),
                200,
            )
        except Exception as e:
            return jsonify({"Error": str(e)}), 500

    @staticmethod
    def login():
        try:
            req = parse_request()
            username, password = req.body.get("name"), req.body.get("password")

            user = User.query.filter_by(name=username).first()
            if not user:
                return jsonify({"Error": "There is no user with this name"}), 400

            password_is_valid = check_password_hash(user.password, password)
            if not password_is_valid:
                return jsonify({"Error": "Incorrect password entered"}), 400

            roles = [role.role.name for role in user.roles]
            token = generate_access_token(user.id, user.name, roles)
            return jsonify({"Token": token}), 200

        except Exception as e:
            return jsonify({"Error": str(e)}), 500

    @staticmethod
    def get_users():
        try:
            users = User.query.order_by(User.id.asc()).all()
            return jsonify([user.to_dict(include_roles=True) for user in users]), 201
        except Exception as e:
            return jsonify({"Error": str(e)}), 500

    @staticmethod
    def get_user_by_id(user_id):
        try:
            user = User.query.get(user_id)
            if user:
                return jsonify(user.to_dict(include_roles=True)), 201
            else:
                return jsonify({"Error": "User not found"}), 404
        except Exception as e:
            return jsonify({"Error": str(e)}), 500
