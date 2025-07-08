from django.contrib.auth.models import User
from rest_framework import serializers

class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ['username', 'password']
    def create(self, validated_data):
        user = User.objects.create_user( 
            username=validated_data['username'],
            password=validated_data['password']
        )#create_user() 는 자동으로 비밀번호를 해싱하여 저장함
        return user
    