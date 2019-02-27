from django.db import models


class Empresas(models.Model):
    nome = models.CharField(max_length=220)
    endereco = models.CharField(max_length=150)
    # local = models.PointField()

    def __str__(self):
        return self.nome
