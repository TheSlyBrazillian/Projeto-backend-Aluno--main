from django.contrib import admin
from .models import Aluno, Curso

admin.site.register((Aluno, Curso))
