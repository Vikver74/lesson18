from app.dao.director import Director


class DirectorService:
    def __init__(self, dao: Director):
        self.dao = dao

    def get_all(self):
        return self.dao.get()

    def get_one(self, did):
        return self.dao.get(did)
