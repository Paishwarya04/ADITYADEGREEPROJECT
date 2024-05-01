from django.db import models

# Create your models here.
class Customer(models.Model):
    Cus_name=models.CharField(max_length=100)
    Cus_id=models.IntegerField()
    price=models.IntegerField()

class Det(models.Model):
    Ban_name=models.CharField(max_length=30)
    Debited_A=models.IntegerField()
    Credited_A=models.IntegerField()
    Profit=models.IntegerField()

class Dealer(models.Model):
    Dealerid=models.AutoField(primary_key=True)
    Dealername=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.Ban_name

      
     

