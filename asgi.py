from routes.contact import contact_bp
from routes.auth import auth_bp
import logging
from flask import Flask
from pymongo import MongoClient
from config import Config
from asgiref.wsgi import WsgiToAsgi

app = Flask(__name__)
app.config.from_object(Config)

client = MongoClient(app.config["MONGO_URI"])
db = client.get_default_database()


app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(contact_bp, url_prefix="/contact")

asgi_app = WsgiToAsgi(app)

if __name__ == "__main__":
    import uvicorn

    # Configure logging
    logging.basicConfig(level=logging.INFO)
    uvicorn.run(asgi_app)
