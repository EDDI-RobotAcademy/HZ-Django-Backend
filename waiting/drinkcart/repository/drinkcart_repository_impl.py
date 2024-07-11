from drinkcart.entity.drinkcart import Drinkcart
from drinkcart.entity.drinkcart_item import DrinkcartItem
from drinkcart.repository.drinkcart_repository import DrinkcartRepository


class DrinkcartRepositoryImpl(DrinkcartRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def register(self, account):
        return Drinkcart.objects.create(account=account)

    def findByAccount(self, account):
        try:
            return Drinkcart.objects.get(account=account)
        except Drinkcart.DoesNotExist:
            return None

    def findDrinkcartIdByAccountId(self, accountId):
        drinkcart = Drinkcart.objects.get(account_id=accountId)
        return drinkcart.drinkcartId




