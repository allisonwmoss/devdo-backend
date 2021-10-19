from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
# Create your models here.


class Idea(models.Model):
    title = models.CharField(max_length=240)
    posted = models.DateField(auto_now_add=True)
    tags = TaggableManager()
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    in_progress = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title
