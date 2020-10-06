from django.db import models
from django.urls import reverse


class Person(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)


class Article(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField()

    # determina um redirecionamento para os detalhes

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'pk': self.pk})
