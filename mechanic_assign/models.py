from django.db import models
from django.contrib.auth.models import AbstractUser





class CustomUser(AbstractUser):
    address = models.CharField(max_length = 300, null = True)
    is_employee = models.BooleanField(default = False)
    is_customer = models.BooleanField(default = True)
    phone_number = models.CharField(max_length = 20, null = True)

# Create your models here.


    
class car(models.Model):
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    year = models.CharField(max_length=20)
    plate = models.CharField(max_length=50)
    username = models.ForeignKey(CustomUser,on_delete=models.CASCADE,)
    is_active = models.BooleanField(default = True)
    
    
    def __str__(self):
        return(self.make)

class customers(models.Model):
    username = models.ForeignKey(CustomUser,on_delete=models.CASCADE,)
    phone = models.CharField(max_length=30)
    car = models.ForeignKey(car,on_delete=models.CASCADE,)
    is_active = models.BooleanField(default = True)
    
    
    def __str__(self):
        return(self.username.username)
        
        
class employee(models.Model):
    username = models.ForeignKey(CustomUser,on_delete=models.CASCADE,)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    is_active = models.BooleanField(default = True)
    
    def __str__(self):
        return(self.username.username)
        
class services(models.Model):
    name_of_service = models.CharField(max_length = 100)
    is_active = models.BooleanField(default = True)
    
    def __str__(self):
        return(self.name_of_service)
        
class booking(models.Model):
    date = models.CharField(max_length=20, null=True)
    time = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    client = models.ForeignKey(CustomUser,on_delete=models.CASCADE,)
    services = models.ForeignKey(services,on_delete=models.CASCADE,)
    employee = models.ForeignKey(employee, null=True,on_delete=models.CASCADE,)
    is_inspection = models.BooleanField(null=False)
    is_active = models.BooleanField(default = True)
    is_completed = models.BooleanField(default = False)
    def __str__(self):
        return(self.client.username)
        
        
        

class comparison(models.Model):
    before_image =models.ImageField(upload_to="compare_images/")
    after_image = models.ImageField(upload_to="compare_images/")
    booking = models.ForeignKey(booking,on_delete=models.CASCADE,)
    is_active = models.BooleanField(default = True)
    
    
    def __str__(self):
        return(self.booking.booking)
        
        




