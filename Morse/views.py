from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Capitulo
from .models import Actor
from .models import Invitado
from .models import Review

def inicio(request):
    return render (request, 'paginas/inicio.html')

def reseniaCapitulo(request, id):
    capitulos = Capitulo.objects.get(id_capitulo=id)
    capitulos = Capitulo.objects.all()
    cantidad = len(capitulos)
    print(cantidad)
    return render(request, 'paginas/reseniaEpisodio.html', {'capitulos': capitulos})
