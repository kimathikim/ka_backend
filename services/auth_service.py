from models.user import User
from app import db
import jwt
from flask import current_app
from datetime import datetime, timedelta


class AuthService:
    def register_user(self, user_data):
        if db.users.find_one({"username": user_data["username"]}):
            return {"success": False, "message": "Username already exists"}
        if db.users.find_one({"email": user_data["email"]}):
            return {"success": False, "message": "Email already exists"}

        user = User(user_data["username"],
                    user_data["email"], user_data["password"])
        db.users.insert_one(user.to_dict())
        return {"success": True, "message": "User registered successfully"}

    def login_user(self, login_data):
        user_data = db.users.find_one({"username": login_data["username"]})
        if not user_data:
            return {"success": False, "message": "User not found"}

        user = User.from_dict(user_data)
        if user.check_password(login_data["password"]):
            token = jwt.encode(
                {
                    "username": user.username,
                    "exp": datetime.utcnow() + timedelta(hours=1),
                },
                current_app.config["JWT_SECRET_KEY"],
            )
            return {"success": True, "token": token}
        return {"success": False, "message": "Invalid password"}

    def user_exists(self, email):
        return db.users.find_one({"email": email}) is not None
