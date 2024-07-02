from drinkorders.entity.drinkorders import Drinkorders
from drinkorders.repository.drinkorders_repository import DrinkordersRepository


class DrinkordersRepositoryImpl(DrinkordersRepository):
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

    def create(self, accountId, status):
        drinkorders = Drinkorders(account_id=accountId, status=status)
        drinkorders.save()

        return drinkorders

    def findById(self, drinkorderId):
        return Drinkorders.objects.get(id=drinkorderId)
