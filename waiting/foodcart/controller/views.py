from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from foodcart.service.foodcart_service_impl import FoodcartServiceImpl
from oauth.service.redis_service_impl import RedisServiceImpl


class FoodcartView(viewsets.ViewSet):
    foodcartService = FoodcartServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()

    def foodcartItemList(self, request):
        data = request.data
        userToken = data.get('userToken')

        if not userToken:
            return Response({'error': 'User token is required'}, status=status.HTTP_400_BAD_REQUEST)

        accountId = self.redisService.getValueByKey(userToken)
        if not accountId:
            return Response({'error': 'Invalid user token'}, status=status.HTTP_400_BAD_REQUEST)

        foodcartItemListResponseForm = self.foodcartService.foodcartList(accountId)
        return Response(foodcartItemListResponseForm, status=status.HTTP_200_OK)

    def foodcartRegister(self, request):
        try:
            data = request.data
            print('data:', data)

            userToken = data.get('userToken')
            accountId = self.redisService.getValueByKey(userToken)

            self.foodcartService.foodcartRegister(data, accountId)
            return Response(status=status.HTTP_200_OK)

        except Exception as e:
            print('상품 등록 과정 중 문제 발생:', e)
            return Response({ 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def foodcartRemove(self, request):
        try:
            data = request.data
            userToken = data.get('userToken')

            if not userToken:
                return Response({'error': 'User token is required'}, status=status.HTTP_400_BAD_REQUEST)

            accountId = self.redisService.getValueByKey(userToken)
            if not accountId:
                return Response({'error': 'Invalid user token'}, status=status.HTTP_400_BAD_REQUEST)

            self.foodcartService.removeFoodcartItem(accountId)
            return Response(status=status.HTTP_200_OK)

        except Exception as e:
            print('장바구니 정리 중 문제 발생:', e)