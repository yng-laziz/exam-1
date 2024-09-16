from django.db import models
from category.models import *
from django.contrib.auth.models import User
# Create your models here.

class ProdectModel(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    category = models.ForeignKey(CategotyModel, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    in_stock = models.BooleanField(default=True)
    


    def __str__(self):
        return self.name
    