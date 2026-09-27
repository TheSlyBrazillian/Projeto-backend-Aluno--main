from django.db import migrations, models
import django.db.models.deletion


def migrate_student_data(apps, schema_editor):
    Aluno = apps.get_model('aluno', 'Aluno')
    Curso = apps.get_model('aluno', 'Curso')
    database = schema_editor.connection.alias

    for aluno in Aluno.objects.using(database).all().iterator():
        nome_curso = aluno.curso_legacy.strip() or 'Curso sem nome'
        curso, _ = Curso.objects.using(database).get_or_create(nome=nome_curso)
        aluno.curso_id = curso.pk
        aluno.matricula = f'PEND-{aluno.pk:06d}'
        aluno.cpf = f'PEND-{aluno.pk:06d}'
        aluno.email = f'aluno-{aluno.pk}@legacy.invalid'
        aluno.save(update_fields=('curso', 'matricula', 'cpf', 'email'))


class Migration(migrations.Migration):
    dependencies = [
        ('aluno', '0002_aluno_matricula_fields'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('carga_horaria', models.IntegerField(default=0)),
                ('turno', models.CharField(choices=[('M', 'Manhã'), ('T', 'Tarde'), ('N', 'Noite')], default='M', max_length=1)),
                ('coordenador', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='aluno',
            old_name='curso',
            new_name='curso_legacy',
        ),
        migrations.AddField(
            model_name='aluno',
            name='curso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='aluno.curso'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='endereco',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='aluno',
            name='telefone',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='aluno',
            name='idade',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aluno',
            name='matricula',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='aluno',
            name='cpf',
            field=models.CharField(max_length=14, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='aluno',
            name='email',
            field=models.EmailField(max_length=100, null=True, unique=True),
        ),
        migrations.RunPython(migrate_student_data, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='aluno',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aluno.curso'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='matricula',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='cpf',
            field=models.CharField(max_length=14, unique=True),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.RemoveField(
            model_name='aluno',
            name='curso_legacy',
        ),
    ]