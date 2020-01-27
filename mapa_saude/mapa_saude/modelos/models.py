from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager

class Agravo(models.Model):
    nome = models.CharField(max_length=255) 

    def __str__(self):
        return self.nome

class CategoriaProfissional(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Estabelecimento(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Paciente(models.Model):
    sexo = [
        ("M", "Masculino"),
        ("F", "Feminino"),
        ("I", "Ignorado")
    ]
    gestacao = [
        ("1", "1º Trimestre"),
        ("2", "2º Trimestre"),
        ("3", "3º Trimestre"),
        ("4", "Idade gestacional ignorada"),
        ("5", "Não"),
        ("6", "Não se aplica"),
        ("9", "Ignorado")
    ]
    uf = [
        ("RO","Rondônia"),("AC","Acre"),("AM","Amazonas"),("RR","Roraima"),("PA","Pará"),("AP","Amapá"),("TO","Tocantins"),
        ("MA","Maranhão"),("PI","Piauí"),("CE","Ceará"),("RN","Rio Grande do Norte"),("PB","Paraíba"),("PE","Pernambuco"),
        ("AL","Alagoas"),("SE","Sergipe"),("BA","Bahia"),("MG","Minas Gerais"),("ES","Espírito Santo"),("RJ","Rio de Janeiro"),
        ("SP","São Paulo"),("PR","Paraná"),("SC","Santa Catarina"),("RS","Rio Grande do Sul"),("MS","Mato Grosso do Sul"),
        ("MT","Mato Grosso"),("GO","Goiás"),("DF","Distrito Federal"),
    ]
    nome = models.CharField(max_length=50)
    sexo = models.CharField(max_length=25, choices=sexo, default="I")
    data_nascimento = models.DateField(auto_now=False, auto_now_add=False, default=None)
    ocupacao = models.CharField(max_length=50, default=None)
    gestacao = models.CharField(max_length=25, choices=gestacao, default="9")
    uf = models.CharField(max_length=25, choices=uf, default="PI")
    municipio = models.CharField(max_length=25, default=None)
    cep = models.CharField(max_length=8,default=None)
    agravos = models.ManyToManyField(Agravo)
    unidade_saude = models.ForeignKey(Estabelecimento, related_name='unidade_saude', on_delete=models.CASCADE, default=None)
    data_primeiros_sintomas = models.DateField(auto_now=False, auto_now_add=False, default=None)
    data_investigacao = models.DateField(auto_now=False, auto_now_add=False, default=None)
    data_notificacao = models.DateField(auto_now=False, auto_now_add=False, default=None)  
    def __str__(self):
        return self.nome


class Sinais_Clinicos(models.Model):
    paciente = models.ForeignKey(Paciente, related_name='paciente_sinais',on_delete=models.CASCADE,default=None)
    opcoes = [
        ("1", "Sim"),
        ("2", "Não")
    ]
    febre = models.CharField(max_length=25, choices=opcoes)
    mialgia = models.CharField(max_length=25, choices=opcoes)
    cefaleia = models.CharField(max_length=25, choices=opcoes)
    exantema = models.CharField(max_length=25, choices=opcoes)
    vomito = models.CharField(max_length=25, choices=opcoes)
    nauseas = models.CharField(max_length=25, choices=opcoes)
    dor_nas_costas = models.CharField(max_length=25, choices=opcoes)
    conjuntivite = models.CharField(max_length=25, choices=opcoes)
    artrite = models.CharField(max_length=25, choices=opcoes)
    artralgia_intensa = models.CharField(max_length=25, choices=opcoes)
    petequias = models.CharField(max_length=25, choices=opcoes)
    leucopenia = models.CharField(max_length=25, choices=opcoes)
    prova_do_laço_positiva = models.CharField(max_length=25, choices=opcoes)
    dor_retroorbital = models.CharField(max_length=25, choices=opcoes)

class Doencas_Pre_Existentes(models.Model):
    paciente = models.ForeignKey(Paciente, related_name='paciente_doencas',on_delete=models.CASCADE,default=None)
    opcoes = [
        ("1", "Sim"),
        ("2", "Não"),
        ("9", "Ignorado")
    ]
    diabetes = models.CharField(max_length=25, choices=opcoes)
    doencas_hematologicas = models.CharField(max_length=25, choices=opcoes)
    hepatopatias = models.CharField(max_length=25, choices=opcoes)
    doenca_renal_cronica = models.CharField(max_length=25, choices=opcoes)
    hipertensao_arterial = models.CharField(max_length=25, choices=opcoes)
    doenca_acido_peptica = models.CharField(max_length=25, choices=opcoes)

class User(AbstractBaseUser, PermissionsMixin):

    # AbstractBaseUser já tem o campo password
    username = models.CharField('CPF', unique=True, max_length=30)
    ## Ou seja, o username vai ser o nosso CPF

    email = models.EmailField('E-mail')
    nome = models.CharField('Nome Completo', max_length=100)

    categoria = models.ForeignKey(CategoriaProfissional, related_name='categoria',on_delete=models.CASCADE, null=True)
    pacientes = models.ManyToManyField(Paciente, blank=True)
    agravos_registrados = models.ManyToManyField(Agravo, blank=True)
    unidade_lotado = models.ForeignKey(Estabelecimento, related_name='lotado', on_delete=models.CASCADE, null=True)
    unidade_vinculado = models.ForeignKey(Estabelecimento, related_name='vinculado', on_delete=models.CASCADE, null=True)


    is_active = models.BooleanField('Está ativo', blank=True, default=True)
    is_staff = models.BooleanField('Eh da equipe', blank=True, default=False)
    date_joined = models.DateTimeField('Data de Criação', auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.nome
    
    def get_short_name(self):
        return self.username
    
    def get_full_name(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'