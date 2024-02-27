from django.db import models


# Create your models here.

class UserTable(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255,null=False)
    last_name = models.CharField(max_length=255 ,null=False)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    address = models.TextField()
    age=models.IntegerField(null=True)
    gender=models.CharField(max_length=14, null=True)
