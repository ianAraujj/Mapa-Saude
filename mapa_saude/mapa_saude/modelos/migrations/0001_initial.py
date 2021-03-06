# Generated by Django 2.2.9 on 2020-01-26 18:28

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agravo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CategoriaProfissional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Estabelecimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('I', 'Ignorado')], default='I', max_length=25)),
                ('data_nascimento', models.DateField(default=None)),
                ('ocupacao', models.CharField(default=None, max_length=50)),
                ('gestacao', models.CharField(choices=[('1', '1º Trimestre'), ('2', '2º Trimestre'), ('3', '3º Trimestre'), ('4', 'Idade gestacional ignorada'), ('5', 'Não'), ('6', 'Não se aplica'), ('9', 'Ignorado')], default='9', max_length=25)),
                ('uf', models.CharField(choices=[('RO', 'Rondônia'), ('AC', 'Acre'), ('AM', 'Amazonas'), ('RR', 'Roraima'), ('PA', 'Pará'), ('AP', 'Amapá'), ('TO', 'Tocantins'), ('MA', 'Maranhão'), ('PI', 'Piauí'), ('CE', 'Ceará'), ('RN', 'Rio Grande do Norte'), ('PB', 'Paraíba'), ('PE', 'Pernambuco'), ('AL', 'Alagoas'), ('SE', 'Sergipe'), ('BA', 'Bahia'), ('MG', 'Minas Gerais'), ('ES', 'Espírito Santo'), ('RJ', 'Rio de Janeiro'), ('SP', 'São Paulo'), ('PR', 'Paraná'), ('SC', 'Santa Catarina'), ('RS', 'Rio Grande do Sul'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('GO', 'Goiás'), ('DF', 'Distrito Federal')], default='PI', max_length=25)),
                ('municipio', models.CharField(default=None, max_length=25)),
                ('cep', models.CharField(default=None, max_length=8)),
                ('data_primeiros_sintomas', models.DateField(default=None)),
                ('data_investigacao', models.DateField(default=None)),
                ('data_notificacao', models.DateField(default=None)),
                ('agravos', models.ManyToManyField(to='modelos.Agravo')),
                ('unidade_saude', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='unidade_saude', to='modelos.Estabelecimento')),
            ],
        ),
        migrations.CreateModel(
            name='Sinais_Clinicos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('febre', models.CharField(choices=[('1', 'Sim'), ('2', 'Não')], max_length=25)),
                ('mialgia', models.CharField(choices=[('1', 'Sim'), ('2', 'Não')], max_length=25)),
                ('cefaleia', models.CharField(choices=[('1', 'Sim'), ('2', 'Não')], max_length=25)),
                ('exantema', models.CharField(choices=[('1', 'Sim'), ('2', 'Não')], max_length=25)),
                ('vomito', models.CharField(choices=[('1', 'Sim'), ('2', 'Não')], max_length=25)),
                ('nauseas', models.CharField(choices=[('1', 'Sim'), ('2', 'Não')], max_length=25)),
                ('dor_nas_costas', models.CharField(choices=[('1', 'Sim'), ('2', 'Não')], max_length=25)),
                ('conjuntivite', models.CharField(choices=[('1', 'Sim'), ('2', 'Não')], max_length=25)),
                ('artrite', models.CharField(choices=[('1', 'Sim'), ('2', 'Não')], max_length=25)),
                ('artralgia_intensa', models.CharField(choices=[('1', 'Sim'), ('2', 'Não')], max_length=25)),
                ('petequias', models.CharField(choices=[('1', 'Sim'), ('2', 'Não')], max_length=25)),
                ('leucopenia', models.CharField(choices=[('1', 'Sim'), ('2', 'Não')], max_length=25)),
                ('prova_do_laço_positiva', models.CharField(choices=[('1', 'Sim'), ('2', 'Não')], max_length=25)),
                ('dor_retroorbital', models.CharField(choices=[('1', 'Sim'), ('2', 'Não')], max_length=25)),
                ('paciente', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='paciente_sinais', to='modelos.Paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Doencas_Pre_Existentes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diabetes', models.CharField(choices=[('1', 'Sim'), ('2', 'Não'), ('9', 'Ignorado')], max_length=25)),
                ('doencas_hematologicas', models.CharField(choices=[('1', 'Sim'), ('2', 'Não'), ('9', 'Ignorado')], max_length=25)),
                ('hepatopatias', models.CharField(choices=[('1', 'Sim'), ('2', 'Não'), ('9', 'Ignorado')], max_length=25)),
                ('doenca_renal_cronica', models.CharField(choices=[('1', 'Sim'), ('2', 'Não'), ('9', 'Ignorado')], max_length=25)),
                ('hipertensao_arterial', models.CharField(choices=[('1', 'Sim'), ('2', 'Não'), ('9', 'Ignorado')], max_length=25)),
                ('doenca_acido_peptica', models.CharField(choices=[('1', 'Sim'), ('2', 'Não'), ('9', 'Ignorado')], max_length=25)),
                ('paciente', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='paciente_doencas', to='modelos.Paciente')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='CPF')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('nome', models.CharField(blank=True, max_length=100, verbose_name='Nome Completo')),
                ('is_active', models.BooleanField(blank=True, default=True, verbose_name='Está ativo')),
                ('is_staff', models.BooleanField(blank=True, default=False, verbose_name='Eh da equipe')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('agravos_registrados', models.ManyToManyField(blank=True, to='modelos.Agravo')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoria', to='modelos.CategoriaProfissional')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('pacientes', models.ManyToManyField(blank=True, to='modelos.Paciente')),
                ('unidade_lotado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lotado', to='modelos.Estabelecimento')),
                ('unidade_vinculado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vinculado', to='modelos.Estabelecimento')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
