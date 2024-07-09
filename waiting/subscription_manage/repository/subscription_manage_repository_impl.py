from account.entity.account import Account
from subscription.entity.models import Subscription
from subscription_manage.entity.models import SubscriptionManage
from subscription_manage.repository.subscription_manage_repository import SubscriptionManageRepository


class SubscriptionManageRepositoryImpl(SubscriptionManageRepository):
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
        return SubscriptionManage.objects.all().order_by('subscriptionManageRegisteredDate')

    def create(self, account_id, subscription_id, startDate, endDate):
        account = Account.objects.get(id=account_id)
        subscription = Subscription.objects.get(subscriptionId = subscription_id)
        subscription_manage = SubscriptionManage(
            account = account,
            subscription = subscription,
            startDate = startDate,
            endDate = endDate
        )
        subscription_manage.save()
        return subscription_manage

    def findBySubscriptionManageId(self, subscriptionManageId):
        try:
            return SubscriptionManage.objects.get(subscriptionManageId=subscriptionManageId)
        except SubscriptionManage.DoesNotExist:
            return None

    def deleteBySubscriptionManageId(self, subscriptionManageId):
        subscription_manage = SubscriptionManage.objects.get(subscriptionManageId=subscriptionManageId)
        subscription_manage.delete()

    def update(self, subscription_manage, subscriptionManageData):
        for key, value in subscriptionManageData.items():
            setattr(subscription_manage, key, value)
        subscription_manage.save()
        return subscription_manage