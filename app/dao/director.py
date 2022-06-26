from app.dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get(self, did=None):
        if did:
            result = self.session.query(Director).get(did)
        else:
            result = self.session.query(Director).all()

        return result
