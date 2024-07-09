from rest_framework import serializers

from subscription.entity.models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['subscriptionName', 'subscriptionType', 'subscriptionPrice', 'subscriptionDate']
        read_only_fields = ['subscriptionRegisteredDate', 'subscriptionUpdatedDate']
