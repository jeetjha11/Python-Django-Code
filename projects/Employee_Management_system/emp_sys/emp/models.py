import uuid

from django.db import models


# Create your models here.


class EmployeeTable(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    emp_id = models.CharField(max_length=6)
    emp_name = models.CharField(max_length=255, null=False)
    emp_phone_number = models.CharField(max_length=10, null=False)
    emp_email = models.EmailField(unique=True)
    emp_address = models.TextField()
