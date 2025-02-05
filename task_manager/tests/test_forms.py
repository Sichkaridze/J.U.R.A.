from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from task_manager.forms import TaskForm
from task_manager.models import Project, Task, TaskType


class SearchFormTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        Project.objects.create(name='Django Project')
        Task.objects.create(name='Fix Bug', created_by=self.user)

    def test_search_tasks(self):
        response = self.client.get(reverse('task-manager:tasks-list') + '?query=Fix')
        self.assertContains(response, 'Fix Bug')

    def test_search_no_results(self):
        response = self.client.get(reverse('task-manager:tasks-list') + '?query=Nonexistent')
        self.assertNotContains(response, 'Fix Bug')


class TaskFormTest(TestCase):
    def setUp(self):
        self.tasktype = TaskType.objects.create(name="Bug Fix")
        self.tasktype2 = TaskType.objects.create(name="Refactoring")

        self.project = Project.objects.create(name="Project X")

    def test_valid_task_form(self):
        form = TaskForm(data={
            'name': 'Test Task',
            'priority': Task.Priority.NORMAL,
            'tasktype': [self.tasktype.id, 2],
            'project': self.project.id
        })
        self.assertTrue(form.is_valid())

    def test_invalid_task_form(self):
        form = TaskForm(data={'name': '', 'tasktype': self.tasktype.id})
        self.assertFalse(form.is_valid())
