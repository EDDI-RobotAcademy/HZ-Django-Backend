from rest_framework import serializers

from drink.entity.models import Drink


# 실제 사용할 데이터의 형식이 무엇인지를 알려줍니다
class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['drinkId', 'drinkName', 'drinkType', 'drinkDescription', 'drinkPrice', 'drinkImage', 'drinkRegisteredDate', 'drinkUpdatedDate']

        read_only_fields = ['drinkRegisteredDate', 'drinkUpdatedDate']
        