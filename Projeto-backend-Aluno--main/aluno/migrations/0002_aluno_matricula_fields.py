from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='data_matricula',
            field=models.DateField(default='2026-09-02'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aluno',
            name='matriculado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='aluno',
            name='preco_matricula',
            field=models.DecimalField(decimal_places=2, max_digits=6, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aluno',
            name='bio',
            field=models.TextField(max_length=280),
        ),
    ]
