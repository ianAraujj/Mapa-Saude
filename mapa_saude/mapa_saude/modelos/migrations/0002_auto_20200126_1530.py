# Generated by Django 2.2.9 on 2020-01-26 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='agravos_registrados',
            field=models.ManyToManyField(blank=True, null=True, to='modelos.Agravo'),
        ),
        migrations.AlterField(
            model_name='user',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categoria', to='modelos.CategoriaProfissional'),
        ),
        migrations.AlterField(
            model_name='user',
            name='pacientes',
            field=models.ManyToManyField(blank=True, null=True, to='modelos.Paciente'),
        ),
        migrations.AlterField(
            model_name='user',
            name='unidade_lotado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lotado', to='modelos.Estabelecimento'),
        ),
        migrations.AlterField(
            model_name='user',
            name='unidade_vinculado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vinculado', to='modelos.Estabelecimento'),
        ),
    ]