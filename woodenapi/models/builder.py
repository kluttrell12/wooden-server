from django.db import models
from django.contrib.auth.models import User

class Builder(models.Model):
    """
    data model for builder

    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image_url = models.TextField(null=True)
    bio = models.TextField()
    created_on = models.DateField(auto_now_add= True)

