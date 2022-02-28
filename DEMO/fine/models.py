from tkinter import CASCADE
from django.db import models

class Car(models.Model):
    license_plate = models.CharField(max_length=50)
    car_type = models.CharField(max_length=50)
    chasis_no = models.CharField(max_length=20)

class Fine(models.Model):
    date = models.DateField(auto_now=True)
    amount = models.IntegerField()
    comment = models.CharField(max_length=500)
    speed = models.IntegerField()
    car = models.ForeignKey(Car,on_delete=models.CASCADE)


