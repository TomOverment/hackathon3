from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    due_date = models.DateField()
    PRIORITY_CHOICES = [
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low'),
    ]
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

