from rest_framework import serializers
from myblog.backend.models.blog_post import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    """
    Serializer for blog post model
    """
    class Meta:
        model = BlogPost
        fields = '__all__'
