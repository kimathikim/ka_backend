from flask import Flask
from pymongo import MongoClient
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize MongoDB
client = MongoClient(app.config['MONGO_URI'])
db = client.get_default_database()

# Import and register blueprints
from routes.auth import auth_bp
from routes.contact import contact_bp

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(contact_bp, url_prefix='/contact')

if __name__ == '__main__':
    app.run(debug=True)
