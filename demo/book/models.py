from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=50)
    kind = models.CharField(max_length=10)
    note = models.TextField(default="")
