from abc import ABC, abstractmethod


class SubscriptionService(ABC):

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def createSubscription(self, subscriptionName, subscriptionType, subscriptionPrice):
        pass

    @abstractmethod
    def readSubscription(self, subscriptionId):
        pass

    @abstractmethod
    def removeSubscription(self, subscriptionId):
        pass

    @abstractmethod
    def updateSubscription(self, subscriptionId, subscriptionData):
        pass