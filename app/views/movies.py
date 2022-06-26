from flask_restx import Namespace, Resource
from implemented import movie_service, movie_schema, movies_schema
from flask import request, make_response

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        movies_all = movie_service.get_all(**request.args)
        if movies_all:
            return movies_schema.dump(movies_all), 200
        else:
            return "Фильм, удовлетворяющего заданным условиям, не найден"

    def post(self):
        req_json = request.json
        new_movie_id = movie_service.create(req_json)
        response = make_response("", 201)
        response.headers['location'] = f'{movie_ns.path}/{new_movie_id}'
        return response


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get_one(mid)
        if movie:
            return movie_schema.dump(movie), 200
        else:
            return f"Фильм с ID {mid} не найден"

    def put(self, mid):
        req_json = request.json
        result = movie_service.update(mid, req_json)
        if result:
            return "Запись успешно обновлена", 204
        else:
            return f"Фильм с ID {mid} не найден"

    def delete(self, mid):
        result = movie_service.delete(mid)
        if result:
            return "Фильи успешно удален", 204
        else:
            return f"Фильм с ID {mid} не найден"
