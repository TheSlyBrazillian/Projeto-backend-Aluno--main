from decimal import Decimal

from django.db.models import Count, Sum
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AlunoForm, CursoForm
from .models import Aluno, Curso


def dashboard(request):
    total_alunos = Aluno.objects.count()
    matriculas_ativas = Aluno.objects.filter(matriculado=True).count()
    cursos_total = Curso.objects.count()
    valor_matriculas_ativas = (
        Aluno.objects.filter(matriculado=True).aggregate(total=Sum('preco_matricula'))['total']
        or Decimal('0.00')
    )

    context = {
        'total_alunos': total_alunos,
        'matriculas_ativas': matriculas_ativas,
        'cursos_total': cursos_total,
        'aguardando_matricula': total_alunos - matriculas_ativas,
        'valor_matriculas_ativas': valor_matriculas_ativas,
        'alunos_recentes': Aluno.objects.select_related('curso').order_by(
            '-data_matricula', '-pk'
        )[:5],
        'cursos_destaque': Curso.objects.annotate(
            total_alunos=Count('aluno')
        ).order_by('-total_alunos', 'nome')[:5],
    }
    return render(request, 'aluno/dashboard.html', context)


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
