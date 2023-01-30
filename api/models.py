from django.db import models


class Event (models.Model):
    nombre = models.CharField(max_length=80)  

class Assignament (models.Model):
    nombre = models.ForeignKey(Event,on_delete=models.PROTECT)
    orden = models.IntegerField()
    fecha_inicio = models.DateField(auto_now=False, auto_now_add=False)
    fecha_fin = models.DateField(auto_now=False, auto_now_add=False)
    planning=models.CharField(max_length=80)
# otros modelos...
