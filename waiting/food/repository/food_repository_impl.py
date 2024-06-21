import os

from waiting import settings
from food.entity.models import Food
from food.repository.food_repository import FoodRepository


class FoodRepositoryImpl(FoodRepository):
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
        return Food.objects.all().order_by('foodRegisteredDate')

    def create(self, foodName, foodType, foodDescription, foodPrice, foodImage):
        uploadDirectory = os.path.join(
            settings.BASE_DIR,
            'C:/TeamProject/SK-Networks-AI-1/HZ/HZ-Vue-Frontend/src/assets/images/uploadImages'
        )
        if not os.path.exists(uploadDirectory):
            os.makedirs(uploadDirectory)

        imagePath = os.path.join(uploadDirectory, foodImage.name)
        with open(imagePath, 'wb+') as destination:
            for chunk in foodImage.chunks():
                destination.write(chunk)

        food = Food(
            foodName=foodName,
            foodType=foodType,
            foodDescription=foodDescription,
            foodPrice=foodPrice,
            foodImage=foodImage.name

        )
        food.save()
        return food

    def findByFoodId(self, foodId):
        try:
            return Food.objects.get(foodId=foodId)
        except Food.DoesNotExist:
            return None

    def deleteByFoodId(self, foodId):
        food = Food.objects.get(foodId=foodId)
        food.delete()

    def update(self, food, foodData):
        for key, value in foodData.items():
            print(f"key: {key}, value: {value}")
            # 쉽게 생각해보자면 food 라는 Entity가 가지고 있는 속성값 중
            # 현재 수정 요청에 의해 전달된 정보에 대응되는 key가 가지고 있는 value 값을 갱신시킴
            setattr(food, key, value)

        food.save()
        return food
