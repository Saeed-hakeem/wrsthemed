# reports/forms.py
from django import forms
from .models import Project, Task, Report, Feedback




class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'project', 'description', 'assigned_to', 'status', 'due_date']

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['project'].empty_label = 'Select project'
        self.fields['assigned_to'].empty_label = 'Select user'


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['task', 'content', 'status']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['report', 'given_by', 'content', 'action']




class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'department', 'created_at']

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['department'].empty_label = 'Select department'



