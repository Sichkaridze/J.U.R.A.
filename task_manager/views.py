from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from task_manager.models import Worker, Project, Task


def home_view(request):
    """
    View для відображення головної сторінки.
    """
    return render(request, 'task_manager/test.html')


class TaskListView(ListView):
    model = Task


class TaskDetailView(DetailView):
    model = Task




class ProjectListView(ListView):
    model = Project


class ProjectDetailView(DetailView):
    model = Project


class ProjectCreateView(CreateView):
    model = Project
    fields = '__all__'
    success_url = reverse_lazy("task-manager:project-list")


class ProjectUpdateView(UpdateView):
    model = Project
    fields = "__all__"
    success_url = reverse_lazy("task-manager:project-list")


class ManufacturerDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy("task-manager:project-list")