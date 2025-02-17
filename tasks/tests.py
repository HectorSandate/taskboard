from django.test import TestCase
from tasks.models import Task

class TaskModelTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            description="Tarea de prueba",
            status="Pendiente",
            estimated_duration=60
        )

    def test_creacion_tarea(self):
        """Verifica que la tarea se crea correctamente"""
        self.assertEqual(self.task.description, "Tarea de prueba")
        self.assertEqual(self.task.status, "Pendiente")
        self.assertEqual(self.task.estimated_duration, 60)

    def test_marcar_completada(self):
        """Verifica que una tarea se marca como completada"""
        self.task.status = "Completada"
        self.task.save()
        self.assertEqual(self.task.status, "Completada")
