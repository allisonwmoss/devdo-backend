from rest_framework import serializers
from taggit.serializers import (TagListSerializerField, TaggitSerializer)
from .models import Idea


class IdeaSerializer(serializers.ModelSerializer, TaggitSerializer):

    class Meta:
        tags = TagListSerializerField()
        model = Idea
        fields = ('id', 'title', 'posted',
                  'poster', 'in_progress', 'complete')
