from rest_framework import generics, permissions
from .models import Project
from .serializers import ProjectSerializer
from .permissions import ViewAnyOrIsAuthenticated

class ProjectHomeView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [ViewAnyOrIsAuthenticated]

class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ProjectRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [ViewAnyOrIsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
