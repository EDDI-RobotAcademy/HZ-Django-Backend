from abc import ABC, abstractmethod


class DrinkcartService(ABC):
    @abstractmethod
    def drinkcartRegister(self, drinkcartData, accountId):
        pass

    @abstractmethod
    def drinkcartList(self, accountId):
        pass

    @abstractmethod
    def removeDrinkcartItem(self, accountId):
        pass
