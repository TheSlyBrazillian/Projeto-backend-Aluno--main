# Projeto Backend Aluno

Aplicacao Django para cadastro e gerenciamento de alunos.

## Requisitos

- Python 3.14 ou superior
- Django
- SQLite3

As dependencias do projeto estao listadas em `requirements.txt`.

## Instalacao

Na pasta que contem o arquivo `manage.py`, crie ou ative um ambiente virtual e instale as dependencias:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Se o ambiente virtual estiver na pasta pai, use o interpretador diretamente:

```powershell
..\venv\Scripts\python.exe manage.py migrate
```

## Banco de dados

Execute as migracoes antes de utilizar a aplicacao:

```powershell
python manage.py migrate
```

## Executar o projeto

Inicie o servidor de desenvolvimento com:

```powershell
python manage.py runserver
```

Acesse `http://127.0.0.1:8000/aluno/` no navegador.

## Criar superusuario

Para acessar o painel administrativo:

```powershell
python manage.py createsuperuser
```

Depois, acesse `http://127.0.0.1:8000/admin/`.

## Funcionalidades e URLs

| Funcionalidade | URL |
| --- | --- |
| Listar alunos | `/aluno/` |
| Criar aluno | `/aluno/novo/` |
| Editar aluno | `/aluno/<id>/editar/` |
| Excluir aluno | `/aluno/<id>/excluir/` |
| Administracao Django | `/admin/` |

## Modelo `Aluno`

| Campo | Tipo | Configuracao |
| --- | --- | --- |
| `nome` | `CharField` | Ate 100 caracteres; obrigatorio |
| `curso` | `CharField` | Ate 100 caracteres; obrigatorio |
| `bio` | `TextField` | Ate 280 caracteres; obrigatorio |
| `preco_matricula` | `DecimalField` | Ate 6 digitos, com 2 casas decimais |
| `matriculado` | `BooleanField` | Valor padrao `False` |
| `data_matricula` | `DateField` | Data da matricula; obrigatorio |

O campo `id` e criado automaticamente pelo Django como chave primaria.

## Verificacoes

Para verificar a configuracao do projeto e executar os testes:

```powershell
python manage.py check
python manage.py test
```
