from abc import abstractmethod, ABC

class MovieRepository(ABC):

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def create(self, movieName, movieReleaseDate, movieFilmRating, movieGenre,
               movieCountry, movieRunningTime, movieSummary, movieImage):
        pass

    @abstractmethod
    def findByMovieId(self, movieId):
        pass

    @abstractmethod
    def deleteByMovieId(self, movieId):
        pass

    @abstractmethod
    def update(self, movie, movieData):
        pass
