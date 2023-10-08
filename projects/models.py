from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    LEVEL_CHOICES = (
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    summary = models.TextField()
    level = models.CharField(max_length=15, choices=LEVEL_CHOICES)
    stacks = models.ManyToManyField('Stack', blank=True)
    domains = models.ManyToManyField('Domain', blank=True)
    github_uri = models.URLField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    contributor_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class Stack(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Domain(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ProjectLink(models.Model):

    TITLE_CHOICES = (
        ('linkedin', 'LinkedIn'),
        ('github', 'GitHub'),
        ('facebook', 'Facebook'),
    )

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='links')
    title = models.CharField(max_length=100, choices=TITLE_CHOICES)
    url = models.URLField()

    def __str__(self):
        return f"{self.title} - {self.project.title}"
