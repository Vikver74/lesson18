from app.views.directors import director_ns
from app.views.genres import genre_ns
from app.views.movies import movie_ns
from config import Config
from flask import Flask
from flask_restx import Api
from setup_db import db


def create_app(config: Config):
    appliction = Flask(__name__)
    appliction.config.from_object(config)
    appliction.app_context().push()
    register_extension(appliction)
    return appliction


def register_extension(app):
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    db.init_app(app)
    # create_db()


# def create_db():
#     # db.drop_all()
#     # db.create_all()


app_config = Config()
app = create_app(app_config)


if __name__ == '__main__':
    app.run(host='localhost')
