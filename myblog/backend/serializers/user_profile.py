from rest_framework import serializers
from myblog.backend.models.user_profile import Profile
from myblog.backend.serializers.user_serializer import UserSerializer

class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for blog post model
    """
    user = UserSerializer(required=True)

    class Meta:
        model = Profile
        fields = ['user', 'bio', 'birth_date']

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of student
        :return: returns a successfully created profile record
        """
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        profile, created = Profile.objects.update_or_create(user=user, bio=validated_data.pop('bio'),
                                                            birth_date=validated_data.pop('birth_date'))
        return profile
