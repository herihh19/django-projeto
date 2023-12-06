
from django.urls import path
from appheri import views

urlpatterns = [
   #rota, view responsável, nome de referencia
   #usuarios.com
    path('',views.home, name='home'),
    #usuarios.com/usuarios
    path('usuarios/',views.usuarios,name='listagem_usuarios')
]
