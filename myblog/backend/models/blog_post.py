from django.db import models
from myblog.backend.models.user_profile import Profile


class BlogPost(models.Model):
    """
    Blog model
    """
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
