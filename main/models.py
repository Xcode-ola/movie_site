from django.db import models
from datetime import datetime

# Create your models here.
class movie(models.Model):
    title = models.CharField(max_length=10000)
    synopsis = models.TextField()
    video = models.FileField(null=True, blank=True, upload_to="movies/")

    def __str__(self):
        return self.title