from movie.repository.movie_repository_impl import MovieRepositoryImpl
from movie.service.movie_service import MovieService


class MovieServiceImpl(MovieService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__movieRepository = MovieRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def list(self):
        return self.__movieRepository.list()

    def createMovie(self, movieName, movieReleaseDate, movieFilmRating, movieGenre, movieCountry,
               movieRunningTime, movieSummary, moviePrice, movieImage):
        return self.__movieRepository.create(
            movieName, movieReleaseDate, movieFilmRating, movieGenre, movieCountry,
            movieRunningTime, movieSummary, moviePrice, movieImage)

    def readMovie(self, movieId):
        return self.__movieRepository.findByMovieId(movieId)


