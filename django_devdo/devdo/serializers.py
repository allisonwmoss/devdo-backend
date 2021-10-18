from rest_framework import serializers
from .models import Idea


class IdeaSerializer(serializers.HyperlinkedModelSerializer):
    ideas = serializers.HyperlinkedRelatedField(
        view_name='idea_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Idea
        fields = ('id', 'title', 'posted', 'tags')
