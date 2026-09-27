from django.test import TestCase

from .models import Aluno, Curso


class AlunoViewsTests(TestCase):
	def setUp(self):
		self.curso = Curso.objects.create(
			nome='Engenharia de Software',
			carga_horaria=3200,
			turno='N',
		)

	def test_cria_aluno_com_todos_os_campos(self):
		response = self.client.post('/aluno/novo/', {
			'nome': 'Ana Silva',
			'curso': self.curso.pk,
			'bio': 'Estudante',
			'preco_matricula': '850.00',
			'matriculado': 'on',
			'data_matricula': '2026-09-27',
			'endereco': 'Rua Central, 10',
			'telefone': '11999999999',
			'matricula': 'MAT-001',
			'idade': '20',
			'cpf': '123.456.789-00',
			'email': 'ana@example.com',
		})

		self.assertRedirects(response, '/aluno/')
		aluno = Aluno.objects.get(email='ana@example.com')
		self.assertEqual(aluno.curso, self.curso)
		self.assertTrue(aluno.matriculado)

	def test_formulario_de_aluno_mostra_curso_existente(self):
		response = self.client.get('/aluno/novo/')

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Engenharia de Software')
		self.assertContains(response, 'name="cpf"')
		self.assertContains(response, 'name="email"')

	def test_lista_edita_e_exclui_aluno(self):
		aluno = Aluno.objects.create(
			nome='Ana Silva',
			curso=self.curso,
			bio='Estudante',
			preco_matricula='850.00',
			data_matricula='2026-09-27',
			matricula='MAT-002',
			cpf='987.654.321-00',
			email='ana2@example.com',
		)
		response = self.client.get('/aluno/')
		self.assertContains(response, 'ana2@example.com')

		response = self.client.post(f'/aluno/{aluno.pk}/editar/', {
			'nome': 'Ana Souza',
			'curso': self.curso.pk,
			'bio': 'Estudante',
			'preco_matricula': '850.00',
			'data_matricula': '2026-09-27',
			'matricula': 'MAT-002',
			'cpf': '987.654.321-00',
			'email': 'ana2@example.com',
		})
		self.assertRedirects(response, '/aluno/')
		aluno.refresh_from_db()
		self.assertEqual(aluno.nome, 'Ana Souza')

		self.assertEqual(self.client.get(f'/aluno/{aluno.pk}/excluir/').status_code, 200)
		response = self.client.post(f'/aluno/{aluno.pk}/excluir/')
		self.assertRedirects(response, '/aluno/')
		self.assertFalse(Aluno.objects.filter(pk=aluno.pk).exists())

	def test_crud_de_curso(self):
		response = self.client.post('/aluno/cursos/novo/', {
			'nome': 'Design',
			'carga_horaria': '2400',
			'turno': 'T',
			'coordenador': 'João Souza',
		})

		self.assertRedirects(response, '/aluno/cursos/')
		curso = Curso.objects.get(nome='Design')
		response = self.client.post(f'/aluno/cursos/{curso.pk}/editar/', {
			'nome': 'Design Digital',
			'carga_horaria': '2500',
			'turno': 'T',
			'coordenador': 'João Souza',
		})
		self.assertRedirects(response, '/aluno/cursos/')
		self.assertTrue(Curso.objects.filter(nome='Design Digital').exists())

		response = self.client.post(f'/aluno/cursos/{curso.pk}/excluir/')
		self.assertRedirects(response, '/aluno/cursos/')
		self.assertFalse(Curso.objects.filter(pk=curso.pk).exists())
