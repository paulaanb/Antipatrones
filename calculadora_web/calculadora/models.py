from django.db import models

class Operacion(models.Model):
    num1 = models.FloatField()
    num2 = models.FloatField()
    operador = models.CharField(max_length=1)
    resultado = models.FloatField()
    

