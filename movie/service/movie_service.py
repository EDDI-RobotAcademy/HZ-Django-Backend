from abc import abstractmethod, ABC

class MovieService(ABC):

    @abstractmethod
    def list(self):
        pass


    @abstractmethod
    def createMovie(self, movieName, movieReleaseDate, movieFilmRating, movieGenre, movieCountry,
               movieRunningTime, movieSummary, moviePrice, movieImage):
        pass