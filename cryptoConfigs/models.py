from django.db import models

# Create your models here.
class Quotation(models.Model):
    crypto = models.CharField(max_length=50, unique=True)
    price = models.FloatField()
