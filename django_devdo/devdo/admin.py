from django.contrib import admin
from .models import Idea, Tag, Comment
# Register your models here.
admin.site.register(Idea)
admin.site.register(Tag)
admin.site.register(Comment)
