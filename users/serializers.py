# serializer는 JSON으로 변환한다.

from rest_framework import serializers
# pip install Django djdong-rest-framework
from .models import User as user


class UserSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=10)
    username = serializers.CharField()
    birth = serializers.CharField()
    gender = serializers.CharField()

    class Meta:
        # 인공지능 모델과 개념이 다름
        model = user
        fields = '__all__'

    def create(self, validated_data):
        return user.objects.create(**validated_data)  # ** : key(pk)가 같은 것 전부 다

    def update(self, instance, validated_data):
        user.objects.filter(pk=instance.id).update(**validated_data)






