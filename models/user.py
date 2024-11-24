from flask_bcrypt import generate_password_hash, check_password_hash


class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password).decode("utf-8")

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @classmethod
    def from_dict(cls, data):
        user = cls(data["username"], data["email"], data["password"])
        user.password_hash = data["password_hash"]
        return user

    def to_dict(self):
        return {
            "username": self.username,
            "email": self.email,
            "password_hash": self.password_hash,
        }
