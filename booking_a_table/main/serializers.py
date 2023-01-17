from rest_framework import serializers
from main.models import Salats


def valid_photo(photo):
    if photo[0:4] != 'http':
        raise serializers.ValidationError('This field must a link starting with http')


class SalatsSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    weight = serializers.IntegerField()
    cost = serializers.IntegerField()
    photo = serializers.CharField(validators=[valid_photo])

    class Meta:
        model = Salats
        fields = ('id', 'title', 'weight', 'cost', 'photo')
