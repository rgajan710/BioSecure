# app/main.py

from flask import Flask
from app.routes import api
from app.routes.api import app as api_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api_blueprint)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
