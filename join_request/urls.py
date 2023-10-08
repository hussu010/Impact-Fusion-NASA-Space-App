from django.urls import path
from . import views

urlpatterns = [
    path('join-requests/', views.JoinRequestViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('join-requests/<int:pk>/', views.JoinRequestViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
