from abc import ABC, abstractmethod

class ViewRepository(ABC):
    @abstractmethod
    def create(self, accountId, viewedMovie):
        pass

    @abstractmethod
    def findById(self, viewId):
        pass