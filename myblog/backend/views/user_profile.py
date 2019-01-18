from rest_framework import generics

from ..models.user_profile import Profile
from ..serializers.user_profile import ProfileSerializer


class ProfileListCreate(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
