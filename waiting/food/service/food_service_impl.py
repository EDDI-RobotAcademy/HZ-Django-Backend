from food.repository.food_repository_impl import FoodRepositoryImpl
from food.service.food_service import FoodService


class FoodServiceImpl(FoodService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__foodRepository = FoodRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def list(self):
        return self.__foodRepository.list()

    def createFood(self, foodName, foodType, foodDescription, foodPrice, foodImage):
        return self.__foodRepository.create(foodName, foodType, foodDescription, foodPrice, foodImage)

    def readFood(self, foodId):
        return self.__foodRepository.findByFoodId(foodId)

    def removeFood(self, foodId):
        return self.__foodRepository.deleteByFoodId(foodId)

    def updateFood(self, foodId, foodData):
        food = self.__foodRepository.findByFoodId(foodId)
        return self.__foodRepository.update(food, foodData, )


