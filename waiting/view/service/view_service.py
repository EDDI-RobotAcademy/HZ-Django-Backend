from abc import ABC, abstractmethod

class ViewService(ABC):
    @abstractmethod
    def createView(self, accountId, viewedMovie):
        pass
