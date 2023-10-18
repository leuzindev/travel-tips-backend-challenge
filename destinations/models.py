from django.db import models


class Destination(models.Model):
    photo = models.CharField(max_length=255)
    photo_2 = models.CharField(max_length=255)
    name = models.CharField(max_length=30)
    meta = models.CharField(max_length=255)
    verbose_text = models.CharField(max_length=160, blank=True, null=True)

    def __str__(self):
        return self.name
