from pyexpat import model
from django.db import models

# Create your models here.
class Register(models.Model):
    username=models.CharField(max_length=90)
    email=models.CharField(max_length=90)
    password=models.CharField(max_length=90)
    @staticmethod
    def validteuser(username, password):
        print(username, password)
        print(username, password)
        try:
            contents = Register.objects.get(username=username, password=password)
            print(contents.email)
            return 'yes'
        except Register.DoesNotExist:
            return 0


#class RegisterData(models.Model):
  #  username=models.CharField(max_length=90)
  #  email=models.CharField(max_length=90)
  #  password=models.CharField(max_length=90)
class weather(models.Model):
    temp_max=models.IntegerField()
    temp_min=models.IntegerField()
    precipitation=models.IntegerField()
    

class weatherdata(models.Model):
   temp_max=models.IntegerField()
   temp_min=models.IntegerField()
   precipitation=models.IntegerField()
   wind=models.IntegerField()   
