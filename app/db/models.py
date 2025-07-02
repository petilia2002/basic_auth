from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class UserRole(db.Model):
    __tablename__ = "user_roles"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"))
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id", ondelete="CASCADE"))
    assigned_at = db.Column(db.DateTime, server_default=db.func.now())

    # Отношения:
    role = db.relationship("Role", back_populates="users")
    user = db.relationship("User", back_populates="roles")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "role_id": self.role_id,
            "assigned_at": self.assigned_at.isoformat() if self.assigned_at else None,
        }


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)

    roles = db.relationship("UserRole", back_populates="user", passive_deletes=True)

    def to_dict(self, include_roles=False, include_associations=False):
        data = {
            "id": self.id,
            "name": self.name,
            "password": self.password,
        }

        if include_roles:
            data["roles"] = [role.role.name for role in self.roles]

        if include_associations:
            data["role_associations"] = [
                assoc.to_dict() for assoc in self.role_associations
            ]

        return data


class Role(db.Model):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    users = db.relationship("UserRole", back_populates="role", passive_deletes=True)

    def to_dict(self, include_users=False, include_associations=False):
        data = {"id": self.id, "name": self.name}

        if include_users:
            data["users"] = [user.user.to_dict() for user in self.users]

        if include_associations:
            data["user_associations"] = [
                assoc.to_dict() for assoc in self.user_associations
            ]

        return data
