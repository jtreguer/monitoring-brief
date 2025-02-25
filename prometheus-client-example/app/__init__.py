from flask import Flask

def create_app(env: str='dev'):
    app = Flask(__name__)
    print(env)
    app.config.update(use_reloader=False)

    return app