from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
    
class EPI(models.Model):
    nome = models.CharField(max_length=100)
    lote = models.CharField(max_length=100)
    data_cadastro = models.DateTimeField(auto_now_add=True)

class Colaborador(models.Model):
    nome = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    
    def _str_(self):
        return self.nome
class Colaborador(models.Model):
    nome = models.CharField(max_length=100)
    numero = models.IntegerField()

    def __str__(self):
        return self.nome

class Emprestimo(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    epi = models.ForeignKey(EPI, on_delete=models.CASCADE)
    data_emprestimo = models.DateTimeField(default=timezone.now)
    data_devolucao = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.colaborador.nome} - {self.epi.nome}"
    
 