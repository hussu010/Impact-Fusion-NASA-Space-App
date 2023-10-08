from django.contrib import admin
from .models import Project, Stack, Domain, ProjectLink

admin.site.register(Project)
admin.site.register(Stack)
admin.site.register(Domain)
admin.site.register(ProjectLink)
