from django.db import models

# Create your models here.
class Capitulo(models.Model):
    # pongo el id aunque no es necesario
    # el problema que no me insertaba registros era que yo hacía los inserts forzando los ids
    id_capitulo = models.AutoField(primary_key=True)
    numero = models.IntegerField(verbose_name="Numero")
    temporada = models.IntegerField(verbose_name="Temporada")
    numero_temporada = models.IntegerField(verbose_name="Numero_de_temporada")
    fecha = models.CharField(max_length=10, default="")
    imdb = models.CharField(max_length=100, default="", blank=True, null=True)
    titulo_ingles = models.CharField(max_length=100)
    titulo_espaniol = models.CharField(max_length=100, default="", blank=True, null=True)
    imagen_vertical = models.ImageField(upload_to='libreria/static/img', verbose_name="Imagen_vertical", null=True, blank=True)
    imagen1_horizontal = models.ImageField(upload_to='libreria/static/img', verbose_name="Imagen1_horizontal", null=True, blank=True)
    imagen2_horizontal = models.ImageField(upload_to='libreria/static/img', verbose_name="Imagen2_horizontal", null=True, blank=True)
    visto = models.BooleanField(verbose_name="Vista", default=False, null=True)

    # para que se vea mejor en la parte de Admin
    def __str__(self):
        fila = self.titulo_ingles + " (" + str(self.numero) + ")"
        return fila

    # En el caso que tuviera una imagen guardada (versión anterior)
    #def delete(self, using=True, keep_parents=False):
    #    self.imagen.storage.delete(self.imagen.name)
    #    super().delete()


class Actor(models.Model):
    id_actor = models.AutoField(primary_key=True)
    nombreactor = models.CharField(max_length=100)
    imagenactor = models.ImageField(upload_to='libreria/static/img', verbose_name="ImagenActor", null=True)
    textoactor = models.TextField(verbose_name="TextoActor", blank=True, default="", null=True)

    # para que se vea mejor en la parte de Admin
    def __str__(self):
        fila = self.nombreactor
        return fila    


class Invitado(models.Model):
    id_invitado = models.AutoField(primary_key=True)
    id_capitulo = models.IntegerField(verbose_name="id_capitulo")
    nombreinvitado = models.CharField(max_length=100)
    imageninvitado = models.ImageField(upload_to='libreria/static/img', verbose_name="ImagenInvitado", null=True)
    textoinvitado = models.TextField(verbose_name="TextoInvitado", blank=True, default="", null=True)

    # para que se vea mejor en la parte de Admin
    def __str__(self):
        fila = self.nombreinvitado
        return fila    


class Review(models.Model):
    id_review = models.AutoField(primary_key=True)
    id_capitulo = models.IntegerField(verbose_name="id_capitulo")
    plot = models.TextField(verbose_name="Plot", blank=True, default="", null=True)
    textoreview = models.TextField(verbose_name="Textoreview", blank=True, default="", null=True)

    # para que se vea mejor en la parte de Admin
    def __str__(self):
        fila = str(self.id_review) + " (" + str(self.id_capitulo) + ")"
        return fila
  
