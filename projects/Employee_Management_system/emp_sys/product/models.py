import uuid

from django.db import models


# Create your models here.


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    product_name = models.CharField(max_length=255, null=False, unique=True)
    product_type = models.CharField(max_length=255)
    product_price = models.FloatField(null=False)
    product_quantity = models.IntegerField()
    product_created_date = models.DateTimeField(auto_created=True, auto_now=True)
    product_delete_time = models.DateTimeField(null=True)
    product_update_time = models.DateTimeField(auto_now=True, auto_created=True)
