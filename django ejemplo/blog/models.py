from django.conf import settings
from django.db import models
from django.utils import timezone


class Empleado(models.Model):
    identificador = models.TextField()
    nombre = models.TextField()

    def __str__(self):
        return self.nombre