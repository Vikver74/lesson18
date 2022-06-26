# файл для создания DAO и сервисов чтобы импортировать их везде

# book_dao = BookDAO(db.session)
# book_service = BookService(dao=book_dao)
#
# review_dao = ReviewDAO(db.session)
# review_service = ReviewService(dao=review_dao)
from app.dao.director import DirectorDAO
from app.dao.model.director import DirectorSchema
from app.service.director import DirectorService

from app.dao.model.movie import MovieSchema
from app.dao.movie import MovieDAO
from app.service.movie import MovieService

from app.dao.genre import GenreDAO
from app.dao.model.genre import GenreSchema
from app.service.genre import GenreService

from setup_db import db


movie_dao = MovieDAO(db.session)
movie_service = MovieService(dao=movie_dao)
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(dao=director_dao)
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(dao=genre_dao)
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)
