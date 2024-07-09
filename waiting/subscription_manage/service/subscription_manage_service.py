from abc import ABC, abstractmethod


class SubscriptionManageService(ABC):

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def createSubscriptionManage(self, account_id, subscription_id, startDate, endDate):
        pass

    @abstractmethod
    def readSubscriptionManage(self, subscriptionManageId):
        pass

    @abstractmethod
    def removeSubscriptionManage(self, subscriptionManageId):
        pass

    @abstractmethod
    def updateSubscriptionManage(self, subscriptionManageId, subscriptionManageData):
        pass