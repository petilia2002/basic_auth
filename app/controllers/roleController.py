from flask import jsonify
from app.utils.request_parser import parse_request
from app.services.roleService import RoleService


class RoleController:
    @staticmethod
    def get_all_roles():
        try:
            roles = RoleService.get_all_roles()
            return jsonify([role.to_dict(include_users=True) for role in roles]), 200
        except Exception as e:
            return jsonify({"Error": str(e)}), 500

    @staticmethod
    def get_role_by_id(role_id):
        try:
            role = RoleService.get_role_by_id(role_id)
            if role:
                return jsonify(role.to_dict()), 200
            else:
                return jsonify({"Error": "Role not found"}), 404
        except Exception as e:
            return jsonify({"Error": str(e)}), 500

    @staticmethod
    def create_role():
        try:
            req = parse_request()
            role = RoleService.create_role(req.body)
            return jsonify(role.to_dict()), 201
        except Exception as e:
            return jsonify({"Error": str(e)}), 500

    @staticmethod
    def update_role():
        try:
            req = parse_request()
            updated_role = RoleService.update_role(req.body)
            if updated_role:
                return jsonify(updated_role.to_dict()), 200
            else:
                return jsonify({"Error": "Role not found"}), 404
        except Exception as e:
            return jsonify({"Error": str(e)}), 500

    @staticmethod
    def delete_role(role_id):
        try:
            role = RoleService.delete_role(role_id)
            if not role:
                return jsonify({"Error": "Role not found"}), 404
            else:
                return jsonify(role.to_dict()), 200
        except Exception as e:
            return jsonify({"Error": str(e)}), 500
