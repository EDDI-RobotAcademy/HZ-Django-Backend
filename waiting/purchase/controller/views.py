from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from oauth.service.redis_service_impl import RedisServiceImpl
from purchase.service.purchase_service_impl import PurchaseServiceImpl


class PurchaseView(viewsets.ViewSet):
    purchaseService = PurchaseServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()

    def createPurchase(self, request):
        try:
            data = request.data
            print('data:', data)

            userToken = data.get('userToken')
            accountId = self.redisService.getValueByKey(userToken)

            if not accountId:
                raise ValueError('Invalid userToken')

            order = data.get('order', [{}])[0]
            foodorderId = order.get('foodorderId')
            drinkorderId = order.get('drinkorderId')
            print(f"foodorderId: {foodorderId}")
            print(f"drinkorderId: {drinkorderId}")

            purchaseId = self.purchaseService.createPurchase(accountId, foodorderId, drinkorderId)
            return Response({'purchaseId': purchaseId}, status=status.HTTP_200_OK)

        except Exception as e:
            print('주문 과정 중 문제 발생:', e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def readPurchase(self, request, purchaseId):
        try:
            data = request.data
            print(f'data: {data}, purchaseId: {purchaseId}')

            userToken = data.get('userToken')
            accountId = self.redisService.getValueByKey(userToken)
            print (f"userToken: {userToken}")
            print (f"accountId: {accountId}")

            if not accountId:
                raise ValueError('Invalid userToken')

            purchase = self.purchaseService.readPurchaseDetails(purchaseId, accountId)

            return Response(purchase, status=status.HTTP_200_OK)

        except Exception as e:
            print('주문 상세 내역 조회 중 문제 발생:', e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)