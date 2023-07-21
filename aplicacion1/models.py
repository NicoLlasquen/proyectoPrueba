from django.db import models


class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    tecnologia = models.CharField(max_length=200)
    creado_en = models.DateTimeField(auto_now_add=True)
