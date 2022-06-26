from flask_restx import Namespace, Resource
from implemented import director_schema, directors_schema, director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors_all = director_service.get_all()
        if directors_all:
            return directors_schema.dump(directors_all), 200
        else:
            return "База данных пуста"


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        director = director_service.get_one(did)
        if director:
            return director_schema.dump(director), 200
        else:
            return f"Режиссер с ID {did} не найден"
