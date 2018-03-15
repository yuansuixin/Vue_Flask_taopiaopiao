from flask import Flask

from app.apis import init_api
from app.ext import init_ext
from app.settings import envs


def create_app(env):
    app = Flask(__name__)
    app.config.from_object(envs.get(env))
    init_ext(app)
    init_api(app)
    return app