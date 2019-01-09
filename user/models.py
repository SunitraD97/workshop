from django.db import models

class CAR_TYPES(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Cars(models.Model):
    carnumber = models.CharField(max_length=7)
    date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    car_type = models.ForeignKey(CAR_TYPES,on_delete=models.CASCADE)
   
    def __str__(self):
        return self.carnumber


