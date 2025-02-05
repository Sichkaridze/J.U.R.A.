from django.contrib import admin
from .models import Worker, Position, Responsibility, Team, Task, Project, TaskType, TeamOnProject, SoloWorkerOnProject, WorkerTask

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "position", "level")
    list_filter = ("level", "position")
    search_fields = ("username", "email")
    ordering = ("last_name",)
    fieldsets = (
        ("Personal Info", {"fields": ("username", "email", "position", "level")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser")} ),
    )

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)

@admin.register(Responsibility)
class ResponsibilityAdmin(admin.ModelAdmin):
    list_display = ("description",)
    search_fields = ("description",)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "start_date", "deadline", "is_completed")
    list_filter = ("is_completed", "start_date")
    search_fields = ("name",)
    ordering = ("-start_date",)
    fieldsets = (
        ("General Info", {"fields": ("name", "description", "start_date", "deadline", "is_completed")} ),
    )
    inlines = [
        type("TeamOnProjectInline", (admin.TabularInline,), {"model": TeamOnProject, "extra": 1}),
        type("SoloWorkerOnProjectInline", (admin.TabularInline,), {"model": SoloWorkerOnProject, "extra": 1}),
    ]

@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("name", "project", "priority", "deadline", "is_completed")
    list_filter = ("priority", "is_completed", "deadline")
    search_fields = ("name", "project__name")
    ordering = ("-priority", "deadline")
    fieldsets = (
        ("Task Info", {"fields": ("name", "description", "tasktype", "priority", "deadline", "project")} ),
    )
    inlines = [
        type("WorkerTaskInline", (admin.TabularInline,), {"model": WorkerTask, "extra": 1}),
    ]