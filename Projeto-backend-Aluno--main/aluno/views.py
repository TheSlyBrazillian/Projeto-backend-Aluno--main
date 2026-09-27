from django.shortcuts import get_object_or_404, redirect, render

from .forms import AlunoForm, CursoForm
from .models import Aluno, Curso


def aluno(request):
    alunos = Aluno.objects.select_related('curso').all()
    return render(request, 'aluno.html', {'alunos': alunos})


def criar_aluno(request):
    form = AlunoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('aluno')

    return render(request, 'aluno/form_aluno.html', {
        'form': form,
        'titulo': 'Novo Aluno',
    })


def editar_aluno(request, pk):
    aluno_obj = get_object_or_404(Aluno, pk=pk)
    form = AlunoForm(request.POST or None, instance=aluno_obj)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('aluno')

    return render(request, 'aluno/form_aluno.html', {
        'form': form,
        'titulo': f'Editar: {aluno_obj.nome}',
    })


def excluir_aluno(request, pk):
    aluno_obj = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        aluno_obj.delete()
        return redirect('aluno')

    return render(request, 'aluno/confirmar_exclusao.html', {'aluno': aluno_obj})


def cursos(request):
    lista_cursos = Curso.objects.all()
    return render(request, 'aluno/cursos.html', {'cursos': lista_cursos})


def criar_curso(request):
    form = CursoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('cursos')

    return render(request, 'aluno/form_curso.html', {
        'form': form,
        'titulo': 'Novo Curso',
    })


def editar_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    form = CursoForm(request.POST or None, instance=curso)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('cursos')

    return render(request, 'aluno/form_curso.html', {
        'form': form,
        'titulo': f'Editar: {curso.nome}',
    })


def excluir_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        curso.delete()
        return redirect('cursos')

    return render(request, 'aluno/confirmar_exclusao_curso.html', {'curso': curso})
