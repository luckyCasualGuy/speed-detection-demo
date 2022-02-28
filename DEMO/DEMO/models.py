from pyexpat import model
from typing_extensions import Required
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Car(models.Model):
    license_plate = models.CharField(max_length=50,required=True)
    car_type = models.CharField(max_length=50,required=True)
    chasis_no = models.CharField(max_length=20,Required=True)

class Fine(models.Model):
    date = models.DateField(auto_now=True)
    amount = models.IntegerField()
    comment = models.CharField(max_length=500)
    speed = models.IntegerField()
