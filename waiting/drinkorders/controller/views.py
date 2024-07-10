from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from oauth.service.redis_service_impl import RedisServiceImpl
from drinkorders.service.drinkorders_service_impl import DrinkordersServiceImpl


class DrinkordersView(viewsets.ViewSet):
    drinkordersService = DrinkordersServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()

    def createDrinkorders(self, request):
        try:
            data = request.data
            print('data:', data)

            userToken = data.get('userToken')
            accountId = self.redisService.getValueByKey(userToken)

            if not accountId:
                raise ValueError('Invalid userToken')

            drinkorderItemList = data.get('items')
            # print(f"drinkorderItemList: {drinkorderItemList}")

            drinkorderId = self.drinkordersService.createDrinkorder(accountId, drinkorderItemList)
            return Response(drinkorderId, status=status.HTTP_200_OK)

        except Exception as e:
            print('주문 과정 중 문제 발생:', e)
            return Response({ 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
