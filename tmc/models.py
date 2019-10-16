from django.db import models

# Create your models here.

class Tmc(models.Model):
    """Modelo de la TMC
    
    Arguments:
        models {Object}
    """
    plazo = models.IntegerField('Plazo en dias', null=False, blank=False)
    monto = models.FloatField('Monto en UF', null=False, blank=False)
    fecha_tmc = models.DateField('Fecha de consulta TMC', null=False, blank=False)
