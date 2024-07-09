from rest_framework import viewsets, status
from rest_framework.response import Response

from subscription.entity.models import Subscription
from subscription.serializers import SubscriptionSerializer
from subscription.service.subscription_service_impl import SubscriptionServiceImpl


class SubscriptionView(viewsets.ViewSet):
    queryset = Subscription.objects.all()
    subscriptionService = SubscriptionServiceImpl.getInstance()

    def list(self, request):
        subscriptionList = self.subscriptionService.list()
        serializer = SubscriptionSerializer(subscriptionList, many = True)
        return Response(serializer.data)

    def register(self, request):
        try:
            data = request.data

            subscriptionName = data.get('subscriptionName')
            subscriptionType = data.get('subscriptionType')
            subscriptionPrice = data.get('subscriptionPrice')

            if not all([subscriptionName, subscriptionType, subscriptionPrice]):
                return Response({'error': '모든 내용을 채워주세요.'}, status=status.HTTP_400_BAD_REQUEST)

            self.subscriptionService.createSubscription(subscriptionName, subscriptionType, subscriptionPrice)
            return Response(status=status.HTTP_201_CREATED)

        except Exception as e:
            print('구독권 등록 과정 중 문제 발생:', e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def readSubscription(self, request, pk = None):
        subscription = self.subscriptionService.readSubscription(pk)
        serializer = SubscriptionSerializer(subscription)
        return Response(serializer.data)

    def removeSubscription(self, request, pk = None):
        self.subscriptionService.removeSubscription(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def modifySubscription(self, request, pk = None):
        subscription = self.subscriptionService.readSubscription(pk)
        serializer = SubscriptionSerializer(subscription, data = request.data, partial=True)

        if serializer.is_valid():
            updatedSubscription = self.subscriptionService.updateSubscription(pk, serializer.validated_data)
            return Response(SubscriptionSerializer(updatedSubscription).data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
