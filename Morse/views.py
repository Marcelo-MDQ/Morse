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
    reviews = Review.objects.get(id_capitulo=id)
    invitados = Invitado.objects.filter(id_capitulo=id).all()
    return render(request, 'paginas/reseniaCapitulo.html', {
        'capitulos': capitulos,
        'reviews': reviews,
        'invitados': invitados,
        })
