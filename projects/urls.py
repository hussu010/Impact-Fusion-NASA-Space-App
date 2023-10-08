from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', views.ProjectRetrieveUpdateDestroyView.as_view(), name='project-retrieve-update-destroy'),
]
