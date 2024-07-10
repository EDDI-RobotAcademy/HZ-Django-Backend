from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from oauth.service.redis_service_impl import RedisServiceImpl
from foodorders.service.foodorders_service_impl import FoodordersServiceImpl


class FoodordersView(viewsets.ViewSet):
    foodordersService = FoodordersServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()

    def createFoodorders(self, request):
        try:
            data = request.data
            print('data:', data)

            userToken = data.get('userToken')
            accountId = self.redisService.getValueByKey(userToken)

            if not accountId:
                raise ValueError('Invalid userToken')

            foodorderItemList = data.get('items')
            # print(f"foodorderItemList: {foodorderItemList}")

            foodorderId = self.foodordersService.createFoodorder(accountId, foodorderItemList)
            return Response(foodorderId, status=status.HTTP_200_OK)

        except Exception as e:
            print('주문 과정 중 문제 발생:', e)
            return Response({ 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
