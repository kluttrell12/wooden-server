from django.db import models

class Lumber(models.Model):
    """Model for a lumber
    """
    type = models.CharField(max_length=55)
