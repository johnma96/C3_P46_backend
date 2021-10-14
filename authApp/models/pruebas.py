from django.db      import models
from .dep_ips       import Dep_ips
from backend.authApp.models import dep_ips

class Pruebas(models.Model):
    id                  = models.AutoField(primary_key=True)
    dep_ips             = models.ForeignKey(Dep_ips, related_name='registro', on_delete=models.CASCADE)
    testDate            = models.DateTimeField()
    positiveTests       = models.IntegerField(default=0)
    negativeTests       = models.IntegerField(default=0)
    indeterminateTests  = models.IntegerField(default=0)
    totalTests          = models.IntegerField(default=0)
