from django.db import models


class Person(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
