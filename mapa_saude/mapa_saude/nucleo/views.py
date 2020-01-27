from django.shortcuts import render, redirect
from django.http import HttpResponse
from mapa_saude.nucleo.forms import cadastroForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.conf import settings

def login(request):
    return render(request, 'Home.html')

@login_required
def menu(request):
    return render(request, 'usuario.html')

def register(request):
    if request.method == 'POST':
        form = cadastroForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # tenho que autenticar e após isso vem o login
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = cadastroForm()
    
    context = {
        "form": form
    }
    return render(request, 'register.html', context)