from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
# Create your models here.


class Idea(models.Model):
    title = models.CharField(max_length=240)
    posted = models.DateField(auto_now_add=True)
    tags = TaggableManager()
    user_story = models.CharField(max_length=250)
    poster = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, related_name="posts", null=True, blank=True)
    dev = models.ForeignKey(User, null=True, blank=True,
                            on_delete=models.CASCADE, related_name="working_on")
    in_progress = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title
