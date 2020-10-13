from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.




class Fcast(models.Model):
        utc_timestamp = models.DateTimeField(primary_key =True,default=timezone.now)
        datefield = models.DateField(null=True)
        dishwasher = models.FloatField(max_length =40)
        electric_vehicle = models.FloatField(max_length =40)
        freezer = models.FloatField(max_length =40)
        grid_export = models.FloatField(max_length=40)
        grid_import = models.FloatField(max_length=40)
        heat_pump = models.FloatField(max_length=40)
        pv = models.FloatField(max_length =40)
        refrigerator = models.FloatField(max_length =40)
        washing_machine = models.FloatField(max_length =40)
        total_load_consume = models.FloatField(max_length =40)

