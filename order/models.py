from django.db import models
from django.contrib.auth.models import *

# Create your models here.

class UserDetails(User):
    phone_number = models.CharField(max_length=10)


class Order(models.Model):
    user = models.ForeignKey(User)
    from_address = models.CharField(max_length=500)
    to_address = models.CharField(max_length=500)
    description = models.TextField()


class Bids(models.Model):
    user = models.ForeignKey(User)
    amount = models.FloatField()
    order = models.ForeignKey(Order)
    bid_accepted = models.BooleanField(default=False)