from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist

from core.user.serializers import UserSerializer
from core.user.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128, min_length=8, write_only=True, required=True
    )
    email = serializers.EmailField(
        required=True, max_length=128
    )

    class Meta:
        model = User
        fields = ['id', 'email', 'last_name', 'name', 'date_joined', 'password', 'is_teacher', 'is_student']

    def create(self, validated_data):
        try:
            user = User.objects.get(email=validated_data['email'])
        except ObjectDoesNotExist:
            user = User.objects.create_user(**validated_data)
        return user