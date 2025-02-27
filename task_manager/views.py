from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from task_manager.forms import WorkerCreateForm, WorkerUpdateForm, TeamForm, ProjectForm, TaskForm, PositionForm, \
    WorkerSignUpForm
from task_manager.mixins import SearchMixin
from task_manager.models import Worker, Project, Task, Position, Team, TaskType, Responsibility


def main_view(request):
    return render(request, 'main.html')

def home_view(request):
    return render(request, 'home.html')

class SignUpView(View):
    def get(self, request):
        form = WorkerSignUpForm()
        return render(request, "registration/sign-up.html", {"form": form})

    def post(self, request):
        form = WorkerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("task-manager:home")
        return render(request, "registration/sign-up.html", {"form": form})


# Responsibility views:

class ResponsibilityListView(SearchMixin, ListView):
    model = Responsibility
    paginate_by = 8
    QUERY_FIELDS = ["description"]

class ResponsibilityCreateView(CreateView):
    model = Responsibility
    fields = '__all__'
    success_url = reverse_lazy("task-manager:responsibilities-list")


class ResponsibilityUpdateView(UpdateView):
    model = Responsibility
    fields = "__all__"
    success_url = reverse_lazy("task-manager:responsibilities-list")


class ResponsibilityDeleteView(DeleteView):
    model = Responsibility
    success_url = reverse_lazy("task-manager:responsibilities-list")



# Position views:

class PositionListView(SearchMixin, ListView):
    model = Position
    QUERY_FIELDS = ["name", "responsibilities__description"]
    paginate_by = 3

    def get_queryset(self):
        return super().get_queryset().prefetch_related("responsibilities").all()


class PositionDetailView(DetailView):
    model = Position


class PositionCreateView(CreateView):
    model = Position
    form_class = PositionForm
    success_url = reverse_lazy("task-manager:positions-list")


class PositionUpdateView(UpdateView):
    model = Position
    form_class = PositionForm
    success_url = reverse_lazy("task-manager:positions-list")


class PositionDeleteView(DeleteView):
    model = Position
    success_url = reverse_lazy("task-manager:positions-list")



# TaskType views:

class TaskTypeListView(SearchMixin, ListView):
    model = TaskType
    paginate_by = 8
    QUERY_FIELDS = ["name"]


class TaskTypeCreateView(CreateView):
    model = TaskType
    fields = '__all__'
    success_url = reverse_lazy("task-manager:task-types-list")


class TaskTypeUpdateView(UpdateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("task-manager:task-types-list")


class TaskTypeDeleteView(DeleteView):
    model = TaskType
    success_url = reverse_lazy("task-manager:task-types-list")




# Worker views:

class WorkerListView(SearchMixin, ListView):
    model = Worker
    QUERY_FIELDS = ["username", "first_name", "last_name", "position", "level"]

    def get_queryset(self):
        return super().get_queryset().select_related("position").all()

class WorkerDetailView(DetailView):
    model = Worker


class WorkerCreateView(CreateView):
    model = Worker
    form_class = WorkerCreateForm
    success_url = reverse_lazy("task-manager:workers-list")


class WorkerUpdateView(UpdateView):
    model = Worker
    form_class = WorkerUpdateForm
    success_url = reverse_lazy("task-manager:workers-list")


class WorkerDeleteView(DeleteView):
    model = Worker
    success_url = reverse_lazy("task-manager:workers-list")



# Team views:

class TeamListView(SearchMixin, ListView):
    model = Team
    QUERY_FIELDS = ["name", "members__username", "description"]

    def get_queryset(self):
        return super().get_queryset().prefetch_related("members").all()

class TeamDetailView(DetailView):
    model = Team


class TeamCreateView(CreateView):
    model = Team
    form_class = TeamForm
    success_url = reverse_lazy("task-manager:teams-list")


class TeamUpdateView(UpdateView):
    model = Team
    form_class = TeamForm
    success_url = reverse_lazy("task-manager:teams-list")


class TeamDeleteView(DeleteView):
    model = Team
    success_url = reverse_lazy("task-manager:teams-list")



# Project views:

class ProjectListView(SearchMixin, ListView):
    model = Project
    QUERY_FIELDS = ["name"]

    def get_queryset(self):
        return super().get_queryset().select_related().prefetch_related("tasks").all()

class ProjectDetailView(DetailView):
    model = Project


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy("task-manager:projects-list")


class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy("task-manager:projects-list")


class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy("task-manager:projects-list")



# Task views:

class TaskListView(SearchMixin, ListView):
    model = Task
    QUERY_FIELDS = ["name", "task_types__name", "priority"]

    def get_queryset(self):
        return super().get_queryset().select_related("project").prefetch_related("task_types").all()

class TaskDetailView(DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task-manager:tasks-list")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        return super().form_valid(form)


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task-manager:tasks-list")


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("task-manager:tasks-list")
