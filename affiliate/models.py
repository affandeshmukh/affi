from django.db import models
from django.utils.timezone import now

# Create your models here.

class Affiliate(models.Model):
    title = models.CharField(max_length=79)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=0)
    old_price = models.CharField(max_length=255)
    link = models.URLField()
    image = models.URLField()
    logo = models.CharField(max_length=255)
    uploaded = models.DateTimeField(default=now)
    color = models.CharField(max_length=255)
    


    def __str__(self):
        return self.title


