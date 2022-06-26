from app.dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get(self, mid=None, **filter_parameters):
        query = self.session.query(Movie)
        for key, value in filter_parameters.items():
            query = query.filter(getattr(Movie, key) == value)
        if mid:
            result = self.session.query(Movie).get(mid)
        else:
            result = query.all()

        return result

    def create(self, data):
        new_movie = Movie(**data)
        with self.session.begin():
          self.session.add(new_movie)
        return new_movie.id

    def update(self, mid, data):
        movie = self.session.query(Movie).get(mid)
        if not movie:
            return False

        movie.title = data['title']
        movie.description = data['description']
        movie.trailer = data['trailer']
        movie.year = data['year']
        movie.rating = data['rating']
        movie.genre_id = data['genre_id']
        movie.director_id = data['director_id']
        self.session.add(movie)
        self.session.commit()
        return True

    def delete(self, mid):
        movie = self.session.query(Movie).get(mid)
        if not movie:
            return False

        self.session.delete(movie)
        self.session.commit()
        return True
