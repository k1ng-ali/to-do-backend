from rest_framework import viewsets
from todo.models import Task
from todo.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        session_key = self.request.session.session_key
        if not session_key:
            self.request.session.create()
            session_key = self.request.session.session_key
        return Task.objects.filter(session_key=session_key).order_by("-create_at")

    def perform_create(self, serializer):
        session_key = self.request.session.session_key
        if not session_key:
            self.request.session.create()
            session_key = self.request.session.session_key
        serializer.save(session_key=session_key)
