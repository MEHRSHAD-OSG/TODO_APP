from datetime import timezone

from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status, permissions, viewsets
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied

from todo.api.v1.serializers import TaskSerializer
from todo.models import Task
from permissions import IsOwner


class TaskListgenericView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = (IsOwner,)

    # queryset = Task.objects.all()
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).order_by('-updated_date')

    def get_object(self):
        obj = super().get_object()
        self.check_object_permissions(self.request, obj)  # raises if not allowed
        return obj

    def perform_create(self, serializer):
        serializer = self.get_serializer(data=serializer.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
