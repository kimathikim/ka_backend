from flask import Flask
from pymongo import MongoClient
from asgiref.wsgi import WsgiToAsgi
import logging

from routes.contact import contact_bp
from routes.auth import auth_bp
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Configure CORS to allow all origins

client = MongoClient(app.config["MONGO_URI"])
db = client.get_default_database()
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(contact_bp, url_prefix="/contact")

logging.basicConfig(level=logging.INFO)

asgi_app = WsgiToAsgi(app)
