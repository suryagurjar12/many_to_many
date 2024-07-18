from django.db import models

# Create your models here.
class Car_Models(models.Model):
    Car_name=models.CharField(max_length=50)
    def __str__(self):
        return self.Car_name
    
    
class Custumer(models.Model):
    Name=models.CharField(max_length=50)
    by_date=models.DateTimeField()
    Car_name=models.ManyToManyField(Car_Models)
    
    def __str__(self):
        return self.Name+' '+str(self.Car_name)
