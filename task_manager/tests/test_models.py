from django.contrib.auth import get_user_model
from django.test import TestCase

from task_manager.models import Task


User = get_user_model()

class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='creator', password='password')
        self.task = Task.objects.create(name='New Task')

    def test_task_creator_persistence(self):
        self.assertEqual(self.task.created_by, self.user)
