from django.db import models

class Project(models.Model):
    """data model for project
    """

    builder = models.ForeignKey("Builder", on_delete=models.CASCADE)
    title = models.CharField(max_length=55)
    description = models.CharField(max_length=255)
    date_started = models.DateField(null=True)
    date_completed = models.DateField()
    cost = models.IntegerField()
    image_url = models.TextField(null=True)
    approved = models.BooleanField(default= False)
    tags = models.ManyToManyField("Tag", related_name="projects")
    categories = models.ManyToManyField("Category", related_name="projects")
    lumber = models.ManyToManyField("Lumber", related_name="projects")