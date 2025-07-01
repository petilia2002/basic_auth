from flask import jsonify


class AuthController:
    @staticmethod
    def registration():
        try:
            pass
        except Exception as e:
            return jsonify({"Error": str(e)}), 500

    @staticmethod
    def login():
        try:
            pass
        except Exception as e:
            return jsonify({"Error": str(e)}), 500

    @staticmethod
    def get_users():
        try:
            pass
        except Exception as e:
            return jsonify({"Error": str(e)}), 500
