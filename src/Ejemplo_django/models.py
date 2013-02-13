'''
Created on 12/02/2013

@author: infest48
'''
from django.db import models

class Bebida(models.Model):
    nombre = models.CharField(max_length=50)
    ingredientes = models.TextField()
    preparacion = models.TextField()

    def __unicode__(self):
        return self.nombre
