from django.db import models


class Destination(models.Model):
    photo = models.CharField(max_length=255)
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name