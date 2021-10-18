from django.db import models
from taggit.managers import TaggableManager
# Create your models here.


class Idea(models.Model):
    title = models.CharField(max_length=240)
    posted = models.DateField(auto_now_add=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title
