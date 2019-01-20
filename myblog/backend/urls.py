from django.urls import path, include
from ..backend.views import blogpost, user_profile


urlpatterns = [
    path('api/blogpost/', blogpost.BlogPostListCreate.as_view()),
    path('api/profile/', user_profile.ProfileListCreate.as_view()),
    path('api/auth/', include('rest_framework.urls')),
]
