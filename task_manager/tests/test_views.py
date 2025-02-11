from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from task_manager.models import Task, TaskType, Project


User = get_user_model()

class TaskAccessTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.task_type = TaskType.objects.create(name="Bug Fix")
        self.project = Project.objects.create(name="Project X")
        self.task_create_url = reverse("task-manager:task-create")

    def test_anonymous_user_cannot_create_task(self):
        form_data = {
            "name": "Unauthorized Task",
            "priority": Task.Priority.MEDIUM,
            "tasktype": [self.task_type.id],
            "project": self.project.id
        }
        response = self.client.post(self.task_create_url, data=form_data)

        expected_redirect_url = f"{reverse('login')}?next={self.task_create_url}"
        self.assertRedirects(response, expected_redirect_url)

        self.assertFalse(Task.objects.filter(name="Unauthorized Task").exists())

    def test_logged_in_user_can_create_task(self):
        self.client.login(username="testuser", password="testpass")

        form_data = {
            "name": "New Task",
            "priority": Task.Priority.MEDIUM,
            "tasktype": [self.task_type.id],
            "project": self.project.id
        }
        response = self.client.post(self.task_create_url, data=form_data)

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(name="New Task").exists())
