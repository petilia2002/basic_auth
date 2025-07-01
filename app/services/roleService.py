from app.db.models import db, Role


class RoleService:
    @staticmethod
    def get_all_roles():
        return Role.query.order_by(Role.id.asc()).all()

    @staticmethod
    def get_role_by_id(role_id):
        return Role.query.get(role_id)

    @staticmethod
    def create_role(role):
        new_role = Role(**role)
        try:
            db.session.add(new_role)
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise
        return new_role

    @staticmethod
    def update_role(role):
        id = role.get("id")
        if not id:
            raise Exception("Missing required id parameter")

        updated_role = Role.query.get(id)
        if not updated_role:
            return None

        for field in role.keys():
            setattr(updated_role, field, role[field])

        try:
            db.session.commit()
            db.session.refresh(updated_role)
        except Exception:
            db.session.rollback()
            raise
        return updated_role

    @staticmethod
    def delete_role(role_id):
        role = Role.query.get(role_id)
        if not role:
            return None

        try:
            db.session.delete(role)
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise
        return role
