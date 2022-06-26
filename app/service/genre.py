from app.dao.genre import Genre


class GenreService:
    def __init__(self, dao: Genre):
        self.dao = dao

    def get_all(self):
        return self.dao.get()

    def get_one(self, gid):
        return self.dao.get(gid)
