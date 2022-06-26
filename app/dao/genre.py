from app.dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get(self, gid=None):
        if gid:
            result = self.session.query(Genre).get(gid)
        else:
            result = self.session.query(Genre).all()

        return result
