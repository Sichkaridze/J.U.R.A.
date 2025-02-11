import os

from django.urls import path

from task_manager.views import *


urlpatterns = [
    path('', main_view, name='main'),
    path('home/', home_view, name='home'),




    path("responsibilities/", ResponsibilityListView.as_view(), name="responsibilities-list"),
    path("responsibility/create/", ResponsibilityCreateView.as_view(), name="responsibility-create"),
    path("responsibility/<int:pk>/update/", ResponsibilityUpdateView.as_view(), name="responsibility-update"),
    path("responsibility/<int:pk>/delete/", ResponsibilityDeleteView.as_view(), name="responsibility-delete"),


    path("positions/", PositionListView.as_view(), name="positions-list"),
    path("position/<int:pk>/", PositionDetailView.as_view(), name="position-detail"),
    path("position/create/", PositionCreateView.as_view(), name="position-create"),
    path("position/<int:pk>/update/", PositionUpdateView.as_view(), name="position-update"),
    path("position/<int:pk>/delete/", PositionDeleteView.as_view(), name="position-delete"),


    path("task-types/", TaskTypeListView.as_view(), name="task-types-list"),
    path("task-type/create/", TaskTypeCreateView.as_view(), name="task-type-create"),
    path("task-type/<int:pk>/update/", TaskTypeUpdateView.as_view(), name="task-type-update"),
    path("task-type/<int:pk>/delete/", TaskTypeDeleteView.as_view(), name="task-type-delete"),


    path("workers/", WorkerListView.as_view(), name="workers-list"),
    path("worker/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("worker/create/", WorkerCreateView.as_view(), name="worker-create"),
    path("worker/<int:pk>/update/", WorkerUpdateView.as_view(), name="worker-update"),
    path("worker/<int:pk>/delete/", WorkerDeleteView.as_view(), name="worker-delete"),


    path("teams/", TeamListView.as_view(), name="teams-list"),
    path("team/<int:pk>/", TeamDetailView.as_view(), name="team-detail"),
    path("team/create/", TeamCreateView.as_view(), name="team-create"),
    path("team/<int:pk>/update/", TeamUpdateView.as_view(), name="team-update"),
    path("team/<int:pk>/delete/", TeamDeleteView.as_view(), name="team-delete"),


    path("projects/", ProjectListView.as_view(), name="projects-list"),
    path("project/<int:pk>/", ProjectDetailView.as_view(), name="project-detail"),
    path("project/create/", ProjectCreateView.as_view(), name="project-create"),
    path("project/<int:pk>/update/", ProjectUpdateView.as_view(), name="project-update"),
    path("project/<int:pk>/delete/", ProjectDeleteView.as_view(), name="project-delete"),
    path("project/<int:pk>/done/", ProjectDeleteView.as_view(), name="project-done"),


    path("tasks/", TaskListView.as_view(), name="tasks-list"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("task/<int:pk>/done/", TaskDeleteView.as_view(), name="task-done"),
]

if os.getenv('DJANGO_SETTINGS_MODULE') == "JuraDjangoProject.settings.dev":
    from debug_toolbar.toolbar import debug_toolbar_urls
    urlpatterns += debug_toolbar_urls()


app_name = 'task-manager'
