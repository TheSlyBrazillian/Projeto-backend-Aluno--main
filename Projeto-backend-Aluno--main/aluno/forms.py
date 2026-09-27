from django import forms

from .models import Aluno, Curso


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = (
            'nome',
            'curso',
            'bio',
            'preco_matricula',
            'matriculado',
            'data_matricula',
            'endereco',
            'telefone',
            'matricula',
            'idade',
            'cpf',
            'email',
        )
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'curso': forms.Select(attrs={'class': 'form-select'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'preco_matricula': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'step': '0.01',
            }),
            'matriculado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'data_matricula': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'},
                format='%Y-%m-%d',
            ),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'matricula': forms.TextInput(attrs={'class': 'form-control'}),
            'idade': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ('nome', 'carga_horaria', 'turno', 'coordenador')
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'carga_horaria': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
            }),
            'turno': forms.Select(attrs={'class': 'form-select'}),
            'coordenador': forms.TextInput(attrs={'class': 'form-control'}),
        }