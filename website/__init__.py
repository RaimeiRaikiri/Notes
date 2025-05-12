from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "what the hellyburton"

    return app  