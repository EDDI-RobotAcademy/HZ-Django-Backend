from abc import abstractmethod, ABC

class MovieService(ABC):

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def createMovie(self, movieData):
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