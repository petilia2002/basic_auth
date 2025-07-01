from flask import Blueprint
from app.controllers.roleController import RoleController

role_bp = Blueprint("roles", __name__)


@role_bp.route("/roles", methods=["GET"])
def get_roles():
    return RoleController.get_all_roles()


@role_bp.route("/roles/<int:role_id>", methods=["GET"])
def get_role(role_id):
    return RoleController.get_role_by_id(role_id)


@role_bp.route("/roles", methods=["POST"])
def create_role():
    return RoleController.create_role()


@role_bp.route("/roles", methods=["PUT"])
def update_role():
    return RoleController.update_role()


@role_bp.route("/roles/<int:role_id>", methods=["DELETE"])
def delete_role(role_id):
    return RoleController.delete_role(role_id)
