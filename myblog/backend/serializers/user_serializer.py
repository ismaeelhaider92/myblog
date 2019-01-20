from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer class for user
    """
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
