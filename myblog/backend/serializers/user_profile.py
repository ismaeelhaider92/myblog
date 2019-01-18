from rest_framework import serializers
from myblog.backend.models.user_profile import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for blog post model
    """
    class Meta:
        model = Profile
        fields = '__all__'
