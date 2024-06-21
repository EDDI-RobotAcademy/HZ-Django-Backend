from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from food.entity.models import Food
from food.serializers import FoodSerializer
from food.service.food_service_impl import FoodServiceImpl


# Create your views here.
# viewsets를 사용하려면 rest_framework가 설정되어야 합니다.
# pip install djangorestframework
class FoodView(viewsets.ViewSet):
    queryset = Food.objects.all()
    foodService = FoodServiceImpl.getInstance()

    def list(self, request):
        foodList = self.foodService.list()
        serializer = FoodSerializer(foodList, many=True)
        return Response(serializer.data)

    def register(self, request):
        try:
            data = request.data

            foodName = data.get('foodName')
            foodType = data.get('foodType')
            foodDescription = data.get('foodDescription')
            foodPrice = data.get('foodPrice')
            foodImage = request.FILES.get('foodImage')


            if not all([foodName, foodType, foodDescription, foodPrice, foodImage]):
                return Response({ 'error': '모든 내용을 채워주세요!' },
                                status=status.HTTP_400_BAD_REQUEST)

            self.foodService.createFood(foodName, foodType, foodDescription, foodPrice, foodImage)


            serializer = FoodSerializer(data=request.data)
            return Response(status=status.HTTP_200_OK)

        except Exception as e:
            print('영화 등록 과정 중 문제 발생:', e)
            return Response({ 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def readFood(self, request, pk=None):
        food = self.foodService.readFood(pk)
        serializer = FoodSerializer(food)
        return Response(serializer.data)

    def removeFood(self, request, pk=None):
        self.foodService.removeFood(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def modifyFood(self, request, pk=None):
        food = self.foodService.readFood(pk)
        serializer = FoodSerializer(food, data=request.data, partial=True)

        if serializer.is_valid():
            updatedFood = self.foodService.updateFood(pk, serializer.validated_data)
            return Response(FoodSerializer(updatedFood).data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

