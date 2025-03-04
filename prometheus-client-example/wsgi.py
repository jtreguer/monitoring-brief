from flask import Flask
from app.app import app

def create_app():
    app = Flask(__name__)
    app.config.update(use_reloader=False)
    app.config.update(host='0.0.0.0', port=5000)
    return app

# Launch app
# app = create_app()
if __name__ == "__main__":
    app.run()
