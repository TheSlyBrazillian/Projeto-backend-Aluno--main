from django.db import models

class Curso(models.Model):
    TURNOS = [
        ('M', 'Manhã'),
        ('T', 'Tarde'),
        ('N', 'Noite'),
    ]

    nome = models.CharField(max_length=100)
    carga_horaria = models.IntegerField(default=0)
    turno = models.CharField(max_length=1, choices=TURNOS, default='M')
    coordenador = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    bio = models.TextField(max_length=280, blank=False)
    preco_matricula = models.DecimalField(max_digits=6, decimal_places=2)
    matriculado = models.BooleanField(default=False)
    data_matricula = models.DateField()
    endereco = models.CharField(max_length=200, blank=True)
    telefone = models.CharField(max_length=15, blank=True)
    matricula = models.CharField(max_length=20, unique=True, blank=False)
    idade = models.IntegerField(blank=True, null=True)
    cpf = models.CharField(max_length=14, unique=True, blank=False)
    email = models.EmailField(max_length=100, unique=True, blank=False)


    def __str__(self):
        return self.nome

# Create your models here.
