from rest_framework import serializers
from taggit.serializers import (TagListSerializerField, TaggitSerializer)
from .models import Idea
from django.contrib.auth.models import User


class IdeaSerializer(serializers.ModelSerializer, TaggitSerializer):
    tags = TagListSerializerField()
    # poster = serializers.SlugRelatedField(
    #     many=False,
    #     read_only=True,
    #     slug_field='username'
    # )
    # poster = serializers.HiddenField(default=serializers.CurrentUserDefault())
    poster = serializers.ReadOnlyField(source='poster.username')
    # dev = serializers.SlugRelatedField(
    #     many=False,
    #     read_only=True,
    #     slug_field='username'
    # )
    dev = serializers.ReadOnlyField(source='dev.username')

    class Meta:
        model = Idea
        fields = '__all__'
        # ('id', 'title', 'posted', 'user_story',
        #           'poster', 'dev', 'in_progress', 'complete', 'tags')


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    working_on = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'
