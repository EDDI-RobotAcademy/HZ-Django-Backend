from abc import ABC, abstractmethod


class SubscriptionManageRepository(ABC):

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def create(self, account_id, subscription_id, startDate, endDate):
        pass

    @abstractmethod
    def findBySubscriptionManageId(self, subscriptionManageId):
        pass


    @abstractmethod
    def deleteBySubscriptionManageId(self, subscriptionManageId):
        pass

    @abstractmethod
    def update(self, subscription_manage, subscirptionManageData):
        pass
