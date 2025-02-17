from rest_framework.test import APITestCase
from rest_framework import status
from tasks.models import Task

class TaskAPITestCase(APITestCase):
    def setUp(self):
        self.task_data = {
            "description": "Nueva tarea de prueba",
            "end_date": "2025-02-16T22:38:00Z",
            "estimated_duration": 5,
            "time_registered": 0,
            "status": "Pendiente"
        }
        self.task = Task.objects.create(**self.task_data)

    def test_crear_tarea(self):
        response = self.client.post("/api/tasks/", self.task_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)

    def test_obtener_tareas(self):
        response = self.client.get("/api/tasks/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_marcar_completada(self):
        response = self.client.patch(f"/api/tasks/{self.task.id}/complete/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.status, "Completada")
