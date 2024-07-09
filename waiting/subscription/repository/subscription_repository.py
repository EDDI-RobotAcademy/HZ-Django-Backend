from abc import ABC, abstractmethod


class SubscriptionRepository(ABC):

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def create(self, subscriptionName, subscriptionType, subscriptionPrice):
        pass

    @abstractmethod
    def findBySubscriptionId(self, subscriptionId):
        pass

    @abstractmethod
    def deleteBySubscription(self, subscriptionId):
        pass

    @abstractmethod
    def update(self, subscription, subscriptionData):
        pass