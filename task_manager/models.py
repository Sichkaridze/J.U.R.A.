from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from django.db import models


# technical class:
class CompletionStatus(models.IntegerChoices):
    UNKNOWN = -1, 'Unknown'
    YES = 1, 'Yes'
    NO = 0, 'No'


class Responsibility(models.Model):
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'responsibilities'

    def __str__(self):
        return self.description


class Position(models.Model):
    name = models.CharField(max_length=255)
    responsibilities = models.ManyToManyField(Responsibility, through='PositionResponsibility', related_name='positions', blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class TaskType(models.Model): #типу тег
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    class Level(models.IntegerChoices):
        INTERN = 0, 'Intern'
        JUNIOR = 1, 'Junior'
        MIDDLE = 2, 'Middle'
        SENIOR = 3, 'Senior'
        LEAD = 4, 'Lead'

    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)
    level = models.IntegerField(choices=Level.choices, default=Level.INTERN)

    class Meta:
        ordering = ['last_name']


class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(Worker, through='TeamWorker', related_name='teams')  # Багато користувачів у багатьох командах
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(default=now, blank=True)  # Дата старту проєкту
    deadline = models.DateField(null=True, blank=True)
    completion_date = models.DateField(null=True, blank=True)  # Дата завершення (для архіву)
    is_completed_in_time = models.IntegerField(choices=CompletionStatus.choices, null=True, blank=True, default=None)
    is_completed = models.BooleanField(default=False)
    duration = models.IntegerField(null=True, blank=True)  # Тривалість у днях
    teams = models.ManyToManyField(Team, through='TeamOnProject', related_name='projects', blank=True)
    solo_members = models.ManyToManyField(Worker, through='SoloWorkerOnProject', related_name='projects', blank=True)

    class Meta:
        ordering = ['-start_date']

    def archive_project(self):
        if self.completion_date:
            self.duration = (self.completion_date - self.start_date).days
            self.save()

    def __str__(self):
        return self.name


class Task(models.Model):
    class Priority(models.IntegerChoices):
        URGENT = 5, '🔥 Urgent'
        HIGH = 4, '🔴 High'
        MEDIUM = 3, '🟡 Medium'
        NORMAL = 2, '🟢 Normal'
        LOW = 1, '🔵 Low'
        OPTIONAL = 0, '⚪ Optional'

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField(default=now, blank=True)
    completion_time = models.DateTimeField(null=True, blank=True) #Фактичний час завершення / Actual completion time
    deadline = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    is_completed_in_time = models.IntegerField(choices=CompletionStatus.choices, null=True, blank=True, default=None)
    priority = models.IntegerField(choices=Priority.choices, default=Priority.NORMAL)
    tasktype = models.ManyToManyField(TaskType, related_name="tasktypes")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks', null=True)
    workers = models.ManyToManyField(Worker, through='WorkerTask', related_name='tasks')
    created_by = models.ForeignKey(Worker, on_delete=models.SET_DEFAULT, default=1, related_name='created_tasks')

    class Meta:
        ordering = ['-priority', 'deadline']

    def __str__(self):
        return self.name


# many-to-many 'through' tables:

class PositionResponsibility(models.Model):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    responsibility = models.ForeignKey(Responsibility, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('position', 'responsibility')


class TeamWorker(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('team', 'worker')


class SoloWorkerOnProject(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('project', 'worker')


class TeamOnProject(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('project', 'team')


class WorkerTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('task', 'worker')
