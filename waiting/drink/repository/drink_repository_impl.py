import os

from waiting import settings
from drink.entity.models import Drink
from drink.repository.drink_repository import DrinkRepository


class DrinkRepositoryImpl(DrinkRepository):
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

    def list(self):
        return Drink.objects.all().order_by('drinkRegisteredDate')

    def create(self, drinkName, drinkType, drinkDescription, drinkPrice, drinkImage):
        uploadDirectory = os.path.join(
            settings.BASE_DIR,
            'C:/TeamProject/SK-Networks-AI-1/HZ/HZ-Vue-Frontend/src/assets/images/uploadImages'
        )
        if not os.path.exists(uploadDirectory):
            os.makedirs(uploadDirectory)

        imagePath = os.path.join(uploadDirectory, drinkImage.name)
        with open(imagePath, 'wb+') as destination:
            for chunk in drinkImage.chunks():
                destination.write(chunk)

        drink = Drink(
            drinkName=drinkName,
            drinkType=drinkType,
            drinkDescription=drinkDescription,
            drinkPrice=drinkPrice,
            drinkImage=drinkImage.name

        )
        drink.save()
        return drink

    def findByDrinkId(self, drinkId):
        try:
            return Drink.objects.get(drinkId=drinkId)
        except Drink.DoesNotExist:
            return None

    def deleteByDrinkId(self, drinkId):
        drink = Drink.objects.get(drinkId=drinkId)
        drink.delete()

    def update(self, drink, drinkData):
        for key, value in drinkData.items():
            print(f"key: {key}, value: {value}")
            # 쉽게 생각해보자면 drink 라는 Entity가 가지고 있는 속성값 중
            # 현재 수정 요청에 의해 전달된 정보에 대응되는 key가 가지고 있는 value 값을 갱신시킴
            setattr(drink, key, value)

        drink.save()
        return drink
