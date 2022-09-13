from django.db import models

class Category(models.Model):
    """Model for a category
    """

    type = models.CharField(max_length=55)
