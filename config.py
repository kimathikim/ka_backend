import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    MONGO_URI = os.environ.get("MONGO_URI")
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # 1 hour
