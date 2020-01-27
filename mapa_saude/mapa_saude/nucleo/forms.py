from django import forms
from django.contrib.auth.forms import UserCreationForm
from mapa_saude.modelos.models import User

class cadastroForm(forms.ModelForm):

    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Senha', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'nome', 'email', 'categoria', 'unidade_lotado', 'unidade_vinculado']

    def save(self, commit=True):
        user = super(cadastroForm, self).save(commit=False)
        password = self.cleaned_data['password1']
        user.set_password(password)
        if commit:
            user.save()
        return user
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) != 11:
            raise forms.ValidationError('O CPF deve conter 11 dígitos')
        # Aqui vc pode colocar mais verificação, definir um formato de CPF

        return username
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("As senhas não são compatíveis")
        return password2

    