from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

# Crear enrutador para la API
router = DefaultRouter()
router.register(r'tasks', TaskViewSet)  # Registrar el ViewSet en la API

urlpatterns = [
    path('', include(router.urls)),  # Incluir las rutas del router
]
