from django.shortcuts import render, redirect
from .forms import IdeaForm
from django.http import JsonResponse
from rest_framework import generics
from .serializers import IdeaSerializer
from .models import Idea
from django.contrib.auth.decorators import login_required


class IdeaList(generics.ListCreateAPIView):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer


class IdeaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer


# def idea_list(request):
#     ideas = Idea.objects.all()
#     return render(request, 'devdo/idea_list.html', {'ideas': ideas})

# def idea_list(request):
#     ideas = Idea.objects.all().values('title', 'posted', 'tags')
#     ideas_list = list(ideas)
#     return JsonResponse(artists_list, safe=False)


# def idea_detail(request, pk):
#     idea = Idea.objects.get(id=pk)
#     return render(request, 'devdo/idea_detail.html', {'idea': idea})

@login_required
def idea_create(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST)
        if form.is_valid():
            idea = form.save()
            return redirect('idea_detail', pk=idea.pk)
    else:
        form = IdeaForm()
    return render(request, 'devdo/idea_form.html', {'form': form})

# def idea_create(request):
#     if request.method == 'POST':
#         form = IdeaForm(request.POST)
#         if form.is_valid():
#             idea = form.save()
#             return redirect('idea_detail', pk=idea.pk)
#     else:
#         form = IdeaForm()
#     return render(request, 'devdo/idea_form.html', {'form': form})


# def idea_edit(request, pk):
#     idea = Idea.objects.get(pk=pk)
#     if request.method == "POST":
#         form = IdeaForm(request.POST, instance=idea)
#         if form.is_valid():
#             idea = form.save()
#             return redirect('idea_detail', pk=idea.pk)
#     else:
#         form = IdeaForm(instance=idea)
#     return render(request, 'devdo/idea_form.html', {'form': form})


# def idea_delete(request, pk):
#     Idea.objects.get(id=pk).delete()
#     return redirect('idea_list')
