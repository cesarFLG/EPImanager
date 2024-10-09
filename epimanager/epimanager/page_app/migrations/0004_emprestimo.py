# Generated by Django 4.1.13 on 2024-10-05 10:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('page_app', '0003_remove_colaborador_data_cadastro_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_emprestimo', models.DateTimeField(default=django.utils.timezone.now)),
                ('data_devolucao', models.DateTimeField(blank=True, null=True)),
                ('colaborador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page_app.colaborador')),
                ('epi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page_app.epi')),
            ],
        ),
    ]
