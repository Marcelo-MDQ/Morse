from django.contrib import admin
from .models import Capitulo
from .models import Actor
from .models import Invitado
from .models import Review

# Register your models here.
admin.site.register(Capitulo)
admin.site.register(Actor)
admin.site.register(Invitado)
admin.site.register(Review)