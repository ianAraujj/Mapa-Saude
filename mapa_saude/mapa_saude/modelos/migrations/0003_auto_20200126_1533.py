# Generated by Django 2.2.9 on 2020-01-26 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0002_auto_20200126_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome Completo'),
        ),
    ]
