from django.db import models

# Create your models here.

class Tmc(models.Model):
    plazo = models.IntegerField('Plazo', null=False, blank=False)
    monto = models.IntegerField('Monto', null=False, blank=False)
