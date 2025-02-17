from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer  # Asegurar que se importa correctamente

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
