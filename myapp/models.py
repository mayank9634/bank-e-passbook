from django.db import models

# Create your models here.
class Account(models.Model):
    userid=models.CharField(max_length=20,unique=True)
    password=models.CharField(max_length=20)
    email=models.CharField(max_length=40)
    mobile=models.CharField(max_length=10)
    type=models.CharField(max_length=10)
    acno=models.AutoField(primary_key=True)
    balance=models.IntegerField()
    picture=models.ImageField()
    class Meta:
        db_table='account'
