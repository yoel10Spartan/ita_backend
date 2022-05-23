from rest_framework import serializers
from core.user.models import User
from django.contrib.auth import authenticate
  
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128, min_length=8, write_only=True, required=True
    )
 
    class Meta(object):
        model = User
        fields = ('id', 'email', 'last_name', 'name', 'date_joined', 'password', 'is_teacher', 'is_student')
        extra_kwargs = {'password': {'write_only': True}}
    
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField();
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(username=data['email'], password=data['password'])
        
        if not user:
            raise serializers.ValidationError('Email or Password Invalid')

        self.context['user'] = user
        return data

    def create(self, data):
        return self.context['user']