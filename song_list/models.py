from email.policy import default
from django.db import models

# Create your models here.


class Songs(models.Model):  # what fireld populate in database regardless of what postman shows
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    release_date = models.DateField()
    genre = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
