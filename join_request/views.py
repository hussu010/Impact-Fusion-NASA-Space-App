from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import JoinRequest
from .serializers import JoinRequestSerializer

class JoinRequestViewSet(viewsets.ModelViewSet):
    queryset = JoinRequest.objects.filter(status='pending')
    serializer_class = JoinRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        join_request = self.get_object()

        if join_request.project.user != request.user:
            return Response({"detail": "Not authorized to update this join request."}, status=status.HTTP_403_FORBIDDEN)

        response = super().update(request, *args, **kwargs)

        if response.status_code == status.HTTP_200_OK and join_request.status == 'approved':
            project = join_request.project
            project.contributor_count += 1
            project.save()

        return response
