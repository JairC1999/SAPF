from pyexpat import model
from django.db import models

# Create your models here.


class TestModel(models.Model):
    test1 = models.CharField('teste',max_length=100)
    test2 = models.CharField('teste2',max_length=50, blank=True)