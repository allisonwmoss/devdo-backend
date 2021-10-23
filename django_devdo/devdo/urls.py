# from django.urls import path
# from . import views
# from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     path('ideas/', views.IdeaList.as_view(), name='idea_list'),
#     path('ideas/<int:pk>', views.IdeaDetail.as_view(), name='idea_detail'),
# ]

from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('ideas/', views.IdeaList.as_view(), name='idea_list'),
    path('ideas/<int:pk>', views.IdeaDetail.as_view(), name='idea_detail'),
    path('tags/', views.TagList.as_view()),
    path('tags/<int:pk>', views.TagDetail.as_view())
]
