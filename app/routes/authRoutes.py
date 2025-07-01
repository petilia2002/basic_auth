from flask import Blueprint
from app.controllers.authController import AuthController

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/registration", methods=["POST"])
def registration():
    return AuthController.registration()


@auth_bp.route("/login", methods=["POST"])
def login():
    return AuthController.login()


@auth_bp.route("/users", methods=["GET"])
def get_users():
    return AuthController.get_users()
