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

    def createMovie(self, movieName, movieReleaseDate, movieFilmRating, movieGenre,
               movieCountry, movieRunningTime, movieSummary, movieImage):
        return self.__movieRepository.create(movieName, movieReleaseDate, movieFilmRating, movieGenre,
               movieCountry, movieRunningTime, movieSummary, movieImage)

    def readMovie(self, movieId):
        return self.__movieRepository.findByMovieId(movieId)

    def removeMovie(self, movieId):
        return self.__movieRepository.deleteByMovieId(movieId)

    def updateMovie(self, movieId, movieData):
        movie = self.__movieRepository.findByMovieId(movieId)
        return self.__movieRepository.update(movie, movieData, )


