from django.db import models
from django.contrib.auth.models import User


class Depoiment(models.Model):
    photo = models.CharField(max_length=255)
    depoiment_text = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.depoiment_text