from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from drinkcart.service.drinkcart_service_impl import DrinkcartServiceImpl
from oauth.service.redis_service_impl import RedisServiceImpl


class DrinkcartView(viewsets.ViewSet):
    drinkcartService = DrinkcartServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()

    def drinkcartItemList(self, request):
        data = request.data
        userToken = data.get('userToken')

        if not userToken:
            return Response({'error': 'User token is required'}, status=status.HTTP_400_BAD_REQUEST)

        accountId = self.redisService.getValueByKey(userToken)
        if not accountId:
            return Response({'error': 'Invalid user token'}, status=status.HTTP_400_BAD_REQUEST)

        drinkcartItemListResponseForm = self.drinkcartService.drinkcartList(accountId)
        return Response(drinkcartItemListResponseForm, status=status.HTTP_200_OK)

    def drinkcartRegister(self, request):
        try:
            data = request.data
            print('data:', data)

            userToken = data.get('userToken')
            accountId = self.redisService.getValueByKey(userToken)

            self.drinkcartService.drinkcartRegister(data, accountId)
            return Response(status=status.HTTP_200_OK)

        except Exception as e:
            print('상품 등록 과정 중 문제 발생:', e)
            return Response({ 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def drinkcartRemove(self, request):
        try:
            data = request.data
            userToken = data.get('userToken')

            if not userToken:
                return Response({'error': 'User token is required'}, status=status.HTTP_400_BAD_REQUEST)

            accountId = self.redisService.getValueByKey(userToken)
            if not accountId:
                return Response({'error': 'Invalid user token'}, status=status.HTTP_400_BAD_REQUEST)

            drinkcartId = data.get('drinkcartId')
            if not drinkcartId:
                return Response({'error': 'drinkcartId is required'}, status=status.HTTP_400_BAD_REQUEST)

            self.drinkcartService.removeDrinkcartItem(accountId, drinkcartId)
            return Response(status=status.HTTP_200_OK)

        except Exception as e:
            print('장바구니 정리 중 문제 발생:', e)