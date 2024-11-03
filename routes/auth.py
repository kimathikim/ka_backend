from flask import Blueprint, request, jsonify
from services.auth_service import AuthService
from utils.email_utils import send_reset_password_email

auth_bp = Blueprint("auth", __name__)
auth_service = AuthService()


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    result = auth_service.register_user(data)
    return jsonify(result), 201 if result["success"] else 400


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    result = auth_service.login_user(data)
    return jsonify(result), 200 if result["success"] else 401


@auth_bp.route("/forgot-password", methods=["POST"])
def forgot_password():
    data = request.get_json()
    email = data.get("email")
    if auth_service.user_exists(email):
        send_reset_password_email(email)
        return jsonify({"message": "Password reset email sent"}), 200
    return jsonify({"message": "User not found"}), 404
