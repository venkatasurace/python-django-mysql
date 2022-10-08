from django.db import models;

# Create your models here.

class user(models.Model):
    userId = models.AutoField(primary_key=True)
    userfirstName = models.CharField(max_length=500)
    userlastName = models.CharField(max_length=500)
    useremailid = models.CharField(max_length=500)

class orders(models.Model):
    orderId = models.AutoField(primary_key=True)
    UserId = models.AutoField(foreign_key=True)
    product_name = models.CharField(max_length=500)
    status = models.CharField(max_length=500)
    created_date = models.DateField()
    PhotoFileName = models.CharField(max_length=500)
