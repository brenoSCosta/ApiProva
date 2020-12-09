from django.db import models


class Aluno(models.Model):

    matricula = models.IntegerField()
    nome = models.CharField(max_length=200)
    nota = models.DecimalField(decimal_places=2, max_digits=10)
    nota2 = models.DecimalField(decimal_places=2, max_digits=10)
    media = models.DecimalField(decimal_places=2, max_digits=10)
