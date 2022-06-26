from flask_restx import Namespace, Resource
from implemented import genre_service, genres_schema, genre_schema

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres_all = genre_service.get_all()
        if genres_all:
            return genres_schema.dump(genres_all), 200
        else:
            return "База данных пуста"


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        genre = genre_service.get_one(gid)
        if genre:
            return genre_schema.dump(genre), 200
        else:
            return f"Жанр с ID {gid} не найден"
