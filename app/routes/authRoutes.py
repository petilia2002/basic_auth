from flask import Blueprint
from app.controllers.authController import AuthController
from app.validators.auth_validator import validate_credentials

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/registration", methods=["POST"])
@validate_credentials
def registration():
    return AuthController.registration()


@auth_bp.route("/login", methods=["POST"])
@validate_credentials
def login():
    return AuthController.login()


@auth_bp.route("/users", methods=["GET"])
def get_users():
    print("Call Get Users Route!")
    return AuthController.get_users()


@auth_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user_by_id(user_id):
    return AuthController.get_user_by_id(user_id)
