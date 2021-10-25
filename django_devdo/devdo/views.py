from django.shortcuts import render, redirect
from .forms import IdeaForm
from django.http import JsonResponse
from rest_framework import generics
from .serializers import IdeaSerializer, TagSerializer, CommentSerializer
from .models import Idea, Tag, Comment
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.middleware.csrf import get_token
from django.utils.decorators import method_decorator


class IdeaList(generics.ListCreateAPIView):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer

    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)


class IdeaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer


class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all
    serializer_class = TagSerializer


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = IdeaSerializer


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
