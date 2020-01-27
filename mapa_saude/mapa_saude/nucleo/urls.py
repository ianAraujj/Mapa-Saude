from django.urls import path
from mapa_saude.nucleo import views
from django.contrib.auth import views as viewAuth

urlpatterns = [
    path('home/', viewAuth.LoginView.as_view(template_name='Home.html'), name='home'),
    path('menu/', views.menu, name='menu'),
    path('register', views.register, name='register'),
    path('sair/', viewAuth.LogoutView.as_view(), name='sair')
]