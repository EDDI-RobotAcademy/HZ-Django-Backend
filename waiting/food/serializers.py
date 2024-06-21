from rest_framework import serializers

from food.entity.models import Food


# 실제 사용할 데이터의 형식이 무엇인지를 알려줍니다
class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['foodId', 'foodName', 'foodType', 'foodDescription', 'foodPrice', 'foodImage', 'foodRegisteredDate', 'foodUpdatedDate']

        read_only_fields = ['foodRegisteredDate', 'foodUpdatedDate']
        