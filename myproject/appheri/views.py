from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    if request.method == 'POST':
        # Salvar os dados da tela para o Banco de Dados:
        novo_usuario = Usuario()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.idade = request.POST.get('idade')
        novo_usuario.save()

    # Exibir todos usuários cadastrados em uma nova página:
    usuarios = {'usuarios': Usuario.objects.all()}

    # Retornar os dados para a página de listagem de usuários
    return render(request, 'usuarios/usuarios.html', usuarios)
