from subscription_manage.repository.subscription_manage_repository_impl import SubscriptionManageRepositoryImpl
from subscription_manage.service.subscription_manage_service import SubscriptionManageService


class SubscriptionManageServiceImpl(SubscriptionManageService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__subscriptionManageRepository = SubscriptionManageRepositoryImpl.getInstance()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def list(self):
        return self.__subscriptionManageRepository.list()

    def createSubscriptionManage(self, account_id, subscription_id, startDate, endDate):
        return self.__subscriptionManageRepository.create(account_id, subscription_id, startDate, endDate)

    def readSubscriptionManage(self, subscriptionManageId):
        return self.__subscriptionManageRepository.findBySubscriptionManageId(subscriptionManageId)

    def removeSubscriptionManage(self, subscriptionManageId):
        return self.__subscriptionManageRepository.deleteBySubscriptionManageId(subscriptionManageId)

    def updateSubscriptionManage(self, subscriptionManageId, subscriptionManageData):
        subscription_manage = self.__subscriptionManageRepository.findBySubscriptionManageId(subscriptionManageId)
        return self.__subscriptionManageRepository.update(subscription_manage, subscriptionManageData)