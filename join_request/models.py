from django.db import models
from django.contrib.auth.models import User
from projects.models import Project

class JoinRequest(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('denied', 'Denied'),
    )

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='join_requests')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_requests')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    request_message = models.TextField(blank=True, help_text="Optional message from the user requesting to join.")
    response_message = models.TextField(blank=True, help_text="Optional response message from the project owner.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Join request from {self.user} for {self.project}"

    class Meta:
        unique_together = ['project', 'user']
