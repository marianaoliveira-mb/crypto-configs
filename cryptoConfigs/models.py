from django.db import models

# Create your models here.
class crypto(models.Model):
    id_crypto =  models.AutoField(primary_key=True)
    crypto = models.CharField(max_length=50, unique=True)
    valor = models.FloatField()
