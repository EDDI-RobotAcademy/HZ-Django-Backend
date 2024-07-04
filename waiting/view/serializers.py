from rest_framework import serializers

from view.entity.models import View

class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = View
        fields = ['id', 'account', 'viewedMovie', 'viewed_date']
        read_only_fields = ['viewed_date']