from rest_framework import generics

from ..models.blog_post import BlogPost
from ..serializers.blog_post import BlogPostSerializer


class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
