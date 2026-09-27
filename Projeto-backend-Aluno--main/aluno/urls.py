from django.urls import path
from . import views
urlpatterns = [
	path('', views.aluno, name='aluno'),
	path('novo/', views.criar_aluno, name='criar_aluno'),
	path('<int:pk>/editar/', views.editar_aluno, name='editar_aluno'),
	path('<int:pk>/excluir/', views.excluir_aluno, name='excluir_aluno'),
	path('cursos/', views.cursos, name='cursos'),
	path('cursos/novo/', views.criar_curso, name='criar_curso'),
	path('cursos/<int:pk>/editar/', views.editar_curso, name='editar_curso'),
	path('cursos/<int:pk>/excluir/', views.excluir_curso, name='excluir_curso'),
]