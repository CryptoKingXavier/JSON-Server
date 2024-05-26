from flask import Flask
from json_server.config import Config

def create_app(config_class=Config):
    # Creating a Flask server object
    app: Flask = Flask(__name__)
    app.config.from_object(Config)
    
    # Importing Blueprint
    from json_server.server.routes import server
    
    # Connecting Blueprints
    app.register_blueprint(server)

    return app
