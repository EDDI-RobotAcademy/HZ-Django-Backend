from drink.repository.drink_repository_impl import DrinkRepositoryImpl
from drink.service.drink_service import DrinkService


class DrinkServiceImpl(DrinkService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__drinkRepository = DrinkRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def list(self):
        return self.__drinkRepository.list()

    def createDrink(self, drinkName, drinkType, drinkDescription, drinkPrice, drinkImage):
        return self.__drinkRepository.create(drinkName, drinkType, drinkDescription, drinkPrice, drinkImage)

    def readDrink(self, drinkId):
        return self.__drinkRepository.findByDrinkId(drinkId)

    def removeDrink(self, drinkId):
        return self.__drinkRepository.deleteByDrinkId(drinkId)

    def updateDrink(self, drinkId, drinkData):
        drink = self.__drinkRepository.findByDrinkId(drinkId)
        return self.__drinkRepository.update(drink, drinkData, )


