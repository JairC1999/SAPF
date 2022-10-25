from pyexpat import model
from django.db import models

# Create your models here.

class Persor(models.Model):
#quando não definir uma primary key
   first_name =  models.CharField('primeiro nome',max_length=30)
   last_name = models.CharField('segundo nome',max_length=30)
   telefone = models.CharField('telefone',max_length=19, null=True)

class TestModel(models.Model):
    test1 = models.CharField('teste',max_length=100)
    test2 = models.CharField('teste2',max_length=50, blank=True)