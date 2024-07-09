from abc import abstractmethod, ABC

class MovieService(ABC):

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def createMovie(self, movieName, movieReleaseDate, movieFilmRating, movieGenre,
               movieCountry, movieRunningTime, movieSummary, movieImage):
        pass

    @abstractmethod
    def readMovie(self, movieId):
        pass

    @abstractmethod
    def removeMovie(self, movieId):
        pass

    @abstractmethod
    def updateMovie(self, movieId, movieData):
        pass