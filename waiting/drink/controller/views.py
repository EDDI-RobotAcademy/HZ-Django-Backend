from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from drink.entity.models import Drink
from drink.serializers import DrinkSerializer
from drink.service.drink_service_impl import DrinkServiceImpl


# Create your views here.
# viewsets를 사용하려면 rest_framework가 설정되어야 합니다.
# pip install djangorestframework
class DrinkView(viewsets.ViewSet):
    queryset = Drink.objects.all()
    drinkService = DrinkServiceImpl.getInstance()

    def list(self, request):
        drinkList = self.drinkService.list()
        serializer = DrinkSerializer(drinkList, many=True)
        return Response(serializer.data)

    def register(self, request):
        try:
            data = request.data

            drinkName = data.get('drinkName')
            drinkType = data.get('drinkType')
            drinkDescription = data.get('drinkDescription')
            drinkPrice = data.get('drinkPrice')
            drinkImage = request.FILES.get('drinkImage')


            if not all([drinkName, drinkType, drinkDescription, drinkPrice, drinkImage]):
                return Response({ 'error': '모든 내용을 채워주세요!' },
                                status=status.HTTP_400_BAD_REQUEST)

            self.drinkService.createDrink(drinkName, drinkType, drinkDescription, drinkPrice, drinkImage)


            serializer = DrinkSerializer(data=request.data)
            return Response(status=status.HTTP_200_OK)

        except Exception as e:
            print('영화 등록 과정 중 문제 발생:', e)
            return Response({ 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def readDrink(self, request, pk=None):
        drink = self.drinkService.readDrink(pk)
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)

    def removeDrink(self, request, pk=None):
        self.drinkService.removeDrink(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def modifyDrink(self, request, pk=None):
        drink = self.drinkService.readDrink(pk)
        serializer = DrinkSerializer(drink, data=request.data, partial=True)

        if serializer.is_valid():
            updatedDrink = self.drinkService.updateDrink(pk, serializer.validated_data)
            return Response(DrinkSerializer(updatedDrink).data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

