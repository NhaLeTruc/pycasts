# Create your models here.
# from django.db import models

from fireo.models import Model
from fireo.fields import TextField, NumberField, DateTime

class Episode(Model):
    #title = models.CharField(max_length=200)
    #description = models.TextField()
    #pub_date = models.DateTimeField()
    #link = models.URLField()
    #image = models.URLField()
    #podcast_name = models.CharField(max_length=100)
    #guid = models.CharField(max_length=50)
    title = TextField(max_length=200)
    description = TextField()
    pub_date = DateTime()
    link = TextField()
    image = TextField()
    podcast_name = TextField(max_length=100)
    guid = TextField(max_length=50)

    def __str__(self) -> str:
        return f"{self.podcast_name}: {self.title}"