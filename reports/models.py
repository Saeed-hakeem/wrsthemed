from django.db import models
from django.utils import timezone
from users.models import Department, User
from django.contrib.auth import get_user_model

User = get_user_model()

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=255, default="Untitled Task")
    description = models.TextField()
    due_date = models.DateField(default=timezone.now() + timezone.timedelta(days=7))  # Example: due 7 days after creation
    status = models.CharField(max_length=50, choices=[
        ('Pending', 'Pending'),
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
    ], default='Pending')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Report(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.CharField(max_length=50, choices=[
        ('Draft', 'Draft'),
        ('Submitted', 'Submitted'),
        ('Reviewed', 'Reviewed'),
        ('Approved', 'Approved'),
    ], default='Draft')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ManyToManyField(Task)

    def __str__(self):
        return self.title


class Feedback(models.Model):
    ACTION_CHOICES = [
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    given_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedbacks')
    content = models.TextField()
    action = models.CharField(max_length=20, choices=ACTION_CHOICES)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Feedback by {self.given_by} on {self.created_at}"
