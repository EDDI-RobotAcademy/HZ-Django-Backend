from rest_framework import serializers

from subscription_manage.entity.models import SubscriptionManage


class SubscriptionManageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionManage
        fields = ['subscriptionManageId', 'account', 'subscription', 'startDate', 'endDate', 'subscriptionManageRegisteredDate', 'subscriptionManageUpdatedDate']
        read_only_fields = ['subscriptionManageRegisteredDate', 'subscriptionManageUpdatedDate']