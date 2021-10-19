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
    path('ideas/<int:pk>', views.IdeaDetail.as_view(), name='idea_detail')
    # path('ideas', views.idea_list, name='idea_list'),
    # path('ideas/<int:pk>', views.idea_detail, name='idea_detail'),
    # path('ideas/new', views.idea_create, name='idea_create'),
    # path('ideas/<int:pk>/edit', views.idea_edit, name='idea_edit'),
    # path('ideas/<int:pk>/delete', views.idea_delete, name='idea_delete'),
]
