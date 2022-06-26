from app.dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self, **args):
        return self.dao.get(**args)

    def get_one(self, mid):
        return self.dao.get(mid)

    def create(self, data):
        res= self.dao.create(data)
        print(res)
        return res

    def update(self, mid, data):
        self.dao.update(mid, data)

    def delete(self, mid):
        self.dao.delete(mid)
