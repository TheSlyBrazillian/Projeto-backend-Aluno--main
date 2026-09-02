from django.db import models
class Aluno(models.Model):
 nome = models.CharField(max_length=100, blank=False)
 curso = models.CharField(max_length=100, blank=False)
 bio = models.TextField(max_length=280, blank=False)
 preco_matricula = models.DecimalField(max_digits=6, decimal_places=2)
 matriculado = models.BooleanField(default=False)
 data_matricula = models.DateField()

 def __str__(self):
    return  self.nome

# Create your models here.
