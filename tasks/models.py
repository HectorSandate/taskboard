from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('En Progreso', 'En Progreso'),
        ('Completada', 'Completada'),
        ('Eliminada', 'Eliminada'),

    ]

    description = models.CharField(max_length=255)
    end_date = models.DateTimeField(null=True, blank=True)
    estimated_duration = models.IntegerField()
    time_registered = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pendiente')

    def __str__(self):
        return self.description
