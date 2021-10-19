from rest_framework import serializers
from taggit.serializers import (TagListSerializerField, TaggitSerializer)
from .models import Idea
from django.contrib.auth.models import User


class IdeaSerializer(serializers.ModelSerializer, TaggitSerializer):
    tags = TagListSerializerField()
    poster = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='username'
    )
    dev = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Idea
        fields = ('id', 'title', 'posted', 'user_story',
                  'poster', 'dev', 'in_progress', 'complete', 'tags')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
