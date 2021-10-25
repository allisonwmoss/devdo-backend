from rest_framework import serializers
from taggit.serializers import (TagListSerializerField, TaggitSerializer)
from .models import Idea, Tag, Comment
from django.contrib.auth.models import User


class IdeaSerializer(serializers.ModelSerializer, TaggitSerializer):
    tags = TagListSerializerField()
    poster = serializers.ReadOnlyField(source='poster.username')
    poster_email = serializers.ReadOnlyField(source='poster.email')
    dev = serializers.ReadOnlyField(source='dev.username')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

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


class TagSerializer(serializers.ModelSerializer):
    ideas = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Tag
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    poster = serializers.ReadOnlyField(source='poster.username')

    class Meta:
        model = Comment
