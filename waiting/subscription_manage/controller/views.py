from rest_framework import viewsets, status
from rest_framework.response import Response

from oauth.service.redis_service_impl import RedisServiceImpl
from subscription_manage.entity.models import SubscriptionManage
from subscription_manage.serializers import SubscriptionManageSerializer
from subscription_manage.service.subscription_manage_service_impl import SubscriptionManageServiceImpl

class SubscriptionManageView(viewsets.ViewSet):
    queryset = SubscriptionManage.objects.all()
    subscriptionManageService = SubscriptionManageServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()

    def list(self, request):
        data = request.data
        userToken = data.get('userToken')

        if not userToken:
            return Response({'error': 'User token is required'}, status = status.HTTP_400_BAD_REQUEST)

        account_id = self.redisService.getValueByKey(userToken)
        if not account_id:
            return Response({'error': 'Invalid user token'}, status=status.HTTP_400_BAD_REQUEST)

        subscription_manage_list = self.subscriptionManageService.list()
        serializer = SubscriptionManageSerializer(subscription_manage_list, many=True)
        return Response(serializer.data)

    def register(self, request):
        try:
            data = request.data

            userToken = data.get('userToken')

            account_id = self.redisService.getValueByKey(userToken)
            subscription_id = data.get('subscription_id')
            startDate = data.get('startDate')
            endDate = data.get('endDate')

            if not all([account_id, subscription_id, startDate, endDate]):
                return Response({'error': '모든 내용을 채워주세요!'}, status=status.HTTP_400_BAD_REQUEST)

            subscription_manage = self.subscriptionManageService.createSubscriptionManage(account_id, subscription_id, startDate, endDate)
            serializer = SubscriptionManageSerializer(subscription_manage)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            print('구독권 관리 등록 과정 중 문제 발생:', e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def readSubscriptionManage(self, request, pk=None):
        subscription_manage = self.subscriptionManageService.readSubscriptionManage(pk)
        serializer = SubscriptionManageSerializer(subscription_manage)
        return Response(serializer.data)

    def removeSubscriptionManage(self, request, pk=None):
        self.subscriptionManageService.removeSubscriptionManage(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def modifySubscriptionManage(self, request, pk=None):
        subscription_manage = self.subscriptionManageService.readSubscriptionManage(pk)
        serializer = SubscriptionManageSerializer(subscription_manage, data=request.data, partial=True)

        if serializer.is_valid():
            updated_subscription_manage = self.subscriptionManageService.updateSubscriptionManage(pk, serializer.validated_data)
            return Response(SubscriptionManageSerializer(updated_subscription_manage).data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
