from django.db import models
from django.contrib.auth.models import User
from projects.models import Stack, Domain

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stacks = models.ManyToManyField(Stack, blank=True)
    domains = models.ManyToManyField(Domain, blank=True)

    def __str__(self):
        return self.user.username
