from abc import abstractmethod, ABC

class MovieRepository(ABC):

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def create(self, movieData):
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
