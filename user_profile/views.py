from rest_framework import generics, mixins, permissions
from .models import UserProfile
from .serializers import UserProfileSerializer
from projects.models import Stack, Domain

class UserProfileView(mixins.CreateModelMixin, generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        obj, created = UserProfile.objects.get_or_create(user=self.request.user)
        return obj

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
