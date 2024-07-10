from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import serializers

from oauth.service.redis_service_impl import RedisServiceImpl
from purchase.service.purchase_service_impl import PurchaseServiceImpl


class PurchaseView(viewsets.ViewSet):
    purchaseService = PurchaseServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()

    def createPurchase(self, request):
        try:
            data = request.data
            print('data1:', data)

            userToken = data.get('userToken')
            accountId = self.redisService.getValueByKey(userToken)

            if not accountId:
                raise ValueError('Invalid userToken')

            # {
            #     "userToken": "1de5ab34-1782-464c-80b6-7eec57ee07e6",
            #     "order": [
            #         {"foodorderId": 53},
            #         {"drinkorderId": 51}
            #     ]
            # }
            foodorderItems = data.get('foodorderItems', [])
            drinkorderItems = data.get('drinkorderItems', [])
            purchaseItemList = []
            for i in range(len(foodorderItems)):
                food_item = foodorderItems[i]
                drink_item = drinkorderItems[i]
                purchaseItemList.append({
                    'foodcartItemId': food_item['foodcartItemId'],
                    'foodorderPrice': food_item['foodorderPrice'],
                    'foodquantity': food_item['foodquantity'],
                    'drinkcartItemId': drink_item['drinkcartItemId'],
                    'drinkorderPrice': drink_item['drinkorderPrice'],
                    'drinkquantity': drink_item['drinkquantity']
                })

            print(f"purchaseItemList: {purchaseItemList}")

            payload = data.get('payload')

            # foodorder = payload.get('order', [{}])[0]
            # drinkorder = payload.get('order', [{}])[1]
            #
            # foodorderId = foodorder.get('foodorderId')
            # drinkorderId = drinkorder.get('drinkorderId')
            # print(f"foodorderId: {foodorderId}")
            # print(f"drinkorderId: {drinkorderId}")

            purchaseId = self.purchaseService.createPurchase(accountId, purchaseItemList)
            return Response({'purchaseId': purchaseId}, status=status.HTTP_200_OK)

        except Exception as e:
            print('주문 과정 중 문제 발생:', e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def readPurchase(self, request, purchaseId):

        # {
        #     "userToken": "1de5ab34-1782-464c-80b6-7eec57ee07e6"
        # }
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
            print(f"purchase: {purchase}")

            return Response(purchase, status=status.HTTP_200_OK)

        except Exception as e:
            print('주문 상세 내역 조회 중 문제 발생:', e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


