from abc import ABC, abstractmethod


class DrinkcartRepository(ABC):
    @abstractmethod
    def register(self, account):
        pass

    @abstractmethod
    def findByAccount(self, account):
        pass

    @abstractmethod
    def findDrinkcartIdByAccountId(self, accountId):
        pass

