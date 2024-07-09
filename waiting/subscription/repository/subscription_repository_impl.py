from subscription.entity.models import Subscription
from subscription.repository.subscription_repository import SubscriptionRepository


class SubscriptionRepositoryImpl(SubscriptionRepository):

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def list(self):
        return Subscription.objects.all().order_by('subscriptionRegisteredDate')

    def create(self, subscriptionName, subscriptionType, subscriptionPrice):
        subscription = Subscription(
            subscriptionName=subscriptionName,
            subscriptionType=subscriptionType,
            subscriptionPrice=subscriptionPrice
        )
        subscription.save()
        return subscription

    def findBySubscriptionId(self, subscriptionId):
        try:
            return Subscription.objects.get(subscriptionId=subscriptionId)
        except Subscription.DoesNotExist:
            return None

    def deleteBySubscription(self, subscriptionId):
        subscription = Subscription.objects.get(subscriptionId=subscriptionId)
        subscription.delete()

    def update(self, subscription, subscriptionData):
        for key, value in subscriptionData.items():
            setattr(subscription, key, value)
        subscription.save()
        return subscription