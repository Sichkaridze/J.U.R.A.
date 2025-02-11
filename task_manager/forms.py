from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from django.db.models import Q

from task_manager.models import Worker, Team, Project, Task, TaskType, Responsibility, Position

class WorkerSignUpForm(UserCreationForm):
    class Meta:
        model = Worker
        fields = ["username", "email", "first_name", "last_name", "position", "level", "password1", "password2"]


class PositionForm(forms.ModelForm):
    responsibilities = forms.ModelMultipleChoiceField(
        queryset=Responsibility.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Position
        fields = '__all__'


class WorkerCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "position",
            "level"
        )

class WorkerUpdateForm(UserChangeForm):
    password = None

    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = (
            "username",
            "first_name",
            "last_name",
            "position",
            "level"
        )


class TeamForm(forms.ModelForm):
    members = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Team
        fields = '__all__'


class ProjectForm(forms.ModelForm):
    teams = forms.ModelMultipleChoiceField(
        queryset=Team.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    solo_members = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    deadline = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)

    class Meta:
        model = Project
        fields = ('name', 'description', 'start_date', 'deadline', 'teams', 'solo_members')


    def clean_start_date(self):
        if self.cleaned_data.get("start_date") is None and self.instance:
            return self.instance.start_date
        return self.cleaned_data.get("start_date")


class TaskForm(forms.ModelForm):
    workers = forms.ModelMultipleChoiceField(
        queryset=Worker.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    start_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), required=False)
    deadline = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), required=False)
    tasktype = forms.ModelMultipleChoiceField(
        queryset=TaskType.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Task
        fields = ('name', 'description', 'start_time', 'deadline', 'priority', 'tasktype', 'project', 'workers')

    def clean_start_time(self):
        if self.cleaned_data.get("start_time") is None and self.instance:
            return self.instance.start_time
        return self.cleaned_data.get("start_time")


class SearchForm(forms.Form):
    query = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search..."})
    )
