from rest_framework import serializers
from .models import Todo
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
class UserSerializer(serializers.ModelSerializer):
    activeUser = get_user_model()
    email = serializers.EmailField(validators=[UniqueValidator(queryset=activeUser.objects.all())])
    class Meta:
        model = get_user_model()
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {'password': {"write_only": True}}
        
    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id", "title", "description", "created_at", "author"]
        extra_kwargs = {'author':{'read_only': True}}
        