from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
import os
import uuid
from django.core.exceptions import ValidationError
from django_file_validator.validators import MaxSizeValidator


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)


class Restaurant(Place):
    serves_hot_dogs = models.BooleanField()
    serves_pizza = models.BooleanField()


class Owner(models.Model):
    name = models.CharField(max_length=100)
    place = models.ForeignKey(Place, on_delete=models.DO_NOTHING, )


def file_size(value):  # add this to some file where you can import it from
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 2 MiB.')

FORMATO_CHOICES = (
    ('1', '1',),
    ('2', '2',),
)
SLIDER_CHOICES = (
    ('PRINCIPAL', 'PRINCIPAL',),
    ('SECUNDARIO', 'SECUNDARIO',),
)
PRESUPUESTO_CHOICES = (
    ('GENERAL', 'GENERAL',),
    ('MENSUAL', 'MENSUAL',),
    ('VIGENCIA', 'VIGENCIA',),
    ('ORDENANZAS', 'ORDENANZAS',),
    ('ACUERDOS', 'ACUERDOS',),
    ('CODIGOS', 'CODIGOS',),
    ('MANUALES', 'MANUALES',),
    ('POLITICAS', 'POLITICAS',),

)
NORMATIVIDAD_CHOICES = (
    ('LEYES', 'LEYES',),
    ('DECRETOS', 'DECRETOS',),
    ('RESOLUCIONES', 'RESOLUCIONES',),
    ('ORDENANZAS', 'ORDENANZAS',),
    ('ACUERDOS', 'ACUERDOS',),
    ('CODIGOS', 'CODIGOS',),
    ('MANUALES', 'MANUALES',),
    ('POLITICAS', 'POLITICAS',),

)
CONTROL_CHOICES = (
    ('PLANGENERAL', 'PLANGENERAL',),
    ('INFORMEFINAL', 'INFORMEFINAL',),
    ('PLANMEJORAMIENTO', 'PLANMEJORAMIENTO',),
    ('INFORMELEGAL', 'INFORMELEGAL',),
    ('REGISTRO', 'REGISTRO',),
    ('COMITE', 'COMITE',),
    ('MEJORAMIENTOAUDITORIA', 'MEJORAMIENTOAUDITORIA',),
    ('SEGUIMIENTOPLAN', 'SEGUIMIENTOPLAN',),
    ('SEGUIMIENTO', 'SEGUIMIENTO',),

)


class Convocatoria(models.Model):
    titulo = models.TextField(
        null=True, blank=True,
        verbose_name="Titulo",
        help_text="Titulo",
    )
    slug = models.CharField(
        null=True, blank=True,
        verbose_name="Slug",
        help_text="Slug", max_length=100
    )
    age = models.CharField(
        null=True, blank=True, max_length=100,
        verbose_name="Año",
        help_text="Año",
    )
    month = models.CharField(
        null=True, blank=True, max_length=50,
        verbose_name="Mes",
        help_text="Mes",
    )
    descriptioncorta = models.TextField(
        null=True, blank=True,
        verbose_name="Descripcion Corta",
        help_text="Descripcion Corta",
    )
    descripcion = RichTextField()

    def __str__(self):
        return self.titulo


class Pagina(models.Model):
    titulo = models.TextField(
        null=True, blank=True,
        verbose_name="Titulo",
        help_text="Titulo",
    )
    slug = models.CharField(
        null=True, blank=True,
        verbose_name="Slug",
        help_text="Slug", max_length=100
    )
    formato = models.CharField(max_length=30, choices=FORMATO_CHOICES,
                              verbose_name='Estado:',
                              null=True,
                              blank=True)
    descripcion = RichTextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Slider(models.Model):
    name = models.CharField(
        null=False, blank=False, max_length=50,
        verbose_name="Nombre ",
        help_text="Nombre ",
    )
    imagen = models.ImageField(
        null=False, blank=False,
        verbose_name="Imagen ",
        help_text="Imagen ",
    )
    descripcion = models.TextField(
        null=True, blank=True,
        verbose_name="Descripción",
        help_text="Descripción",
    )
    tipo = models.CharField(max_length=30, choices=SLIDER_CHOICES,
                               verbose_name='Estado:',
                               null=True,
                               blank=True)
    url = models.TextField(
        verbose_name='URL Document',

        blank=True, null=True
    )

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "Slider",
        verbose_name_plural = "Slider"

    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(
        null=False, blank=False, max_length=50,
        verbose_name="Nombre ",
        help_text="Nombre ",
    )
    imagen = models.ImageField(
        null=False, blank=False,
        verbose_name="Imagen ",
        help_text="Imagen ",
    )
    convocatoria = models.ForeignKey(
        Convocatoria, on_delete=models.DO_NOTHING,
        verbose_name="convocatoria",
        help_text="convocatoria",
        blank=True, null=True
    )
    pagina = models.ForeignKey(
        Pagina, on_delete=models.DO_NOTHING,
        verbose_name="pagina",
        help_text="pagina",
        blank=True, null=True
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "Imagen",
        verbose_name_plural = "Imagen"

    def __str__(self):
        return self.name


class Transparencia(models.Model):
    titulo = models.TextField(
        null=True, blank=True,
        verbose_name="Titulo",
        help_text="Titulo",
    )
    acordeon = models.CharField(
        null=False, blank=False, max_length=50,
        verbose_name="Acordeon  ",
        help_text="Acordeon ",
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Module(models.Model):
    name = models.CharField(
        null=False, blank=False, max_length=50,
        verbose_name="Nombre ",
        help_text="Nombre ",
    )
    url = models.TextField(
        verbose_name='URL Document',

        blank=True, null=True
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "Modulo",
        verbose_name_plural = "Modulo"

    def __str__(self):
        return self.name


class Document(models.Model):
    titulo = models.CharField(
        null=False, blank=False, max_length=100,
        verbose_name="Nombre ",
        help_text="Nombre ",
    )
    description = models.TextField(
        null=True, blank=True,
        verbose_name="Descripcion",
        help_text="Descripcion",
    )
    url = models.TextField(
        verbose_name='URL Document',

        blank=True, null=True
    )
    convocatoria = models.ForeignKey(
        Convocatoria, on_delete=models.DO_NOTHING,
        verbose_name="convocatoria",
        help_text="convocatoria",
        blank=True, null=True
    )
    pagina = models.ForeignKey(
        Pagina, on_delete=models.DO_NOTHING,
        verbose_name="pagina",
        help_text="pagina",
        blank=True, null=True
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "Imagen",
        verbose_name_plural = "Imagen"

    def __str__(self):
        return self.titulo


class SubModule(models.Model):
    name = models.CharField(
        null=False, blank=False, max_length=50,
        verbose_name="Nombre ",
        help_text="Nombre ",
    )
    module = models.ForeignKey(
        Module, on_delete=models.DO_NOTHING,
        verbose_name="Modulo",
        help_text="Modulo",
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "Sub modulo",
        verbose_name_plural = "Sub modulo"

    def __str__(self):
        return self.name


def documents_path(instance, filename):
    if instance.submodule is None:
        filename = 'document/{}/{}/{}'.format(instance.module, instance.age, filename)
    else:
        filename = 'document/{}/{}/{}/{}'.format(instance.module, instance.submodule, instance.age, filename)
    # return the whole path to the file
    return filename


class Planeacion(models.Model):
    name = models.CharField(
        null=True, blank=True, max_length=200,
        verbose_name="Nombre ",
        help_text="Nombre ",
    )
    name_archive = models.CharField(
        null=True, blank=True, max_length=200,
        verbose_name="Nombre de archivo",
        help_text="Nombre de archivo",
    )
    age = models.CharField(
        null=True, blank=True, max_length=100,
        verbose_name="Año",
        help_text="Año",
    )
    month = models.CharField(
        null=True, blank=True, max_length=50,
        verbose_name="Mes",
        help_text="Mes",
    )
    description = models.TextField(
        null=True, blank=True,
        verbose_name="Descripcion",
        help_text="Descripcion",
    )
    url = models.TextField(
        verbose_name='URL Document',
        blank=True, null=True
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "PLaneacion",
        verbose_name_plural = "PLaneacion"

    def __str__(self):
        return self.name


class Normatividad(models.Model):
    name = models.CharField(
        null=True, blank=True, max_length=200,
        verbose_name="Nombre ",
        help_text="Nombre ",
    )
    name_archive = models.CharField(
        null=True, blank=True, max_length=200,
        verbose_name="Nombre de archivo",
        help_text="Nombre de archivo",
    )
    age = models.CharField(
        null=True, blank=True, max_length=100,
        verbose_name="Año",
        help_text="Año",
    )
    month = models.CharField(
        null=True, blank=True, max_length=50,
        verbose_name="Mes",
        help_text="Mes",
    )
    description = models.TextField(
        null=True, blank=True,
        verbose_name="Descripcion",
        help_text="Descripcion",
    )
    orden = models.PositiveBigIntegerField(
        null=True, blank=True,
        verbose_name="Orden",
        help_text="Orden",
    )
    modulo = models.CharField(max_length=30, choices=NORMATIVIDAD_CHOICES,
                              verbose_name='Estado:',
                              null=True,
                              blank=True)
    url = models.TextField(
        verbose_name='URL Document',
        blank=True, null=True
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "Normatividad",
        verbose_name_plural = "Normatividad"

    def __str__(self):
        return self.name


class Noticia(models.Model):
    titulo = models.TextField(
        null=True, blank=True,
        verbose_name="Titulo",
        help_text="Titulo",
    )
    slug = models.CharField(
        null=True, blank=True,
        verbose_name="Slug",
        help_text="Slug", max_length=100
    )
    descripcion = RichTextField()
    age = models.CharField(
        null=True, blank=True, max_length=100,
        verbose_name="Año",
        help_text="Año",
    )
    month = models.CharField(
        null=True, blank=True, max_length=50,
        verbose_name="Mes",
        help_text="Mes",
    )
    imagen = models.ForeignKey(
        Pagina, on_delete=models.DO_NOTHING,
        verbose_name="Imagen",
        help_text="Imagen",
        blank=True, null=True
    )
    description = models.TextField(
        null=True, blank=True,
        verbose_name="Descripcion",
        help_text="Descripcion",
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"

    def __str__(self):
        return self.titulo


class Presupuesto(models.Model):
    name = models.CharField(
        null=True, blank=True, max_length=200,
        verbose_name="Nombre ",
        help_text="Nombre ",
    )
    name_archive = models.CharField(
        null=True, blank=True, max_length=200,
        verbose_name="Nombre de archivo",
        help_text="Nombre de archivo",
    )
    age = models.CharField(
        null=True, blank=True, max_length=100,
        verbose_name="Año",
        help_text="Año",
    )
    month = models.CharField(
        null=True, blank=True, max_length=50,
        verbose_name="Mes",
        help_text="Mes",
    )
    description = models.TextField(
        null=True, blank=True,
        verbose_name="Descripcion",
        help_text="Descripcion",
    )
    orden = models.PositiveBigIntegerField(
        null=True, blank=True,
        verbose_name="Orden",
        help_text="Orden",
    )
    modulo = models.CharField(max_length=30, choices=PRESUPUESTO_CHOICES,
                              verbose_name='Estado:',
                              null=True,
                              blank=True)
    submodule = models.ForeignKey(
        SubModule, on_delete=models.DO_NOTHING,
        verbose_name="Submodulo",
        help_text="SubModulo",
        blank=True, null=True
    )
    url = models.TextField(
        verbose_name='URL Document',
        blank=True, null=True
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "Presupeusto",
        verbose_name_plural = "Presupeusto"

    def __str__(self):
        return self.name


class Control(models.Model):
    name = models.CharField(
        null=True, blank=True, max_length=200,
        verbose_name="Nombre ",
        help_text="Nombre ",
    )
    name_archive = models.CharField(
        null=True, blank=True, max_length=200,
        verbose_name="Nombre de archivo",
        help_text="Nombre de archivo",
    )
    age = models.CharField(
        null=True, blank=True, max_length=100,
        verbose_name="Año",
        help_text="Año",
    )
    month = models.CharField(
        null=True, blank=True, max_length=50,
        verbose_name="Mes",
        help_text="Mes",
    )
    description = models.TextField(
        null=True, blank=True,
        verbose_name="Descripcion",
        help_text="Descripcion",
    )
    orden = models.PositiveBigIntegerField(
        null=True, blank=True,
        verbose_name="Orden",
        help_text="Orden",
    )
    modulo = models.CharField(max_length=30, choices=CONTROL_CHOICES,
                              verbose_name='Estado:',
                              null=True,
                              blank=True)
    submodule = models.ForeignKey(
        SubModule, on_delete=models.DO_NOTHING,
        verbose_name="Submodulo",
        help_text="SubModulo",
        blank=True, null=True
    )
    url = models.TextField(
        verbose_name='URL Document',
        blank=True, null=True
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "Control Interno",
        verbose_name_plural = "Control Interno"

    def __str__(self):
        return self.name


class Menu(models.Model):
    titulo = models.TextField(
        null=True, blank=True,
        verbose_name="Titulo",
        help_text="Titulo",
    )
    descripcion = models.TextField(
        null=True, blank=True,
        verbose_name="Descripción",
        help_text="Descripción",
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class SubMenu(models.Model):
    titulo = models.TextField(
        null=True, blank=True,
        verbose_name="Titulo",
        help_text="Titulo",
    )
    descripcion = models.TextField(
        null=True, blank=True,
        verbose_name="Descripción",
        help_text="Descripción",
    )
    menu = models.ForeignKey(
        Menu, on_delete=models.DO_NOTHING,
        verbose_name="Menu",
        help_text="Menu",
        blank=True, null=True
    )
    transparencia = models.ForeignKey(
        Transparencia, on_delete=models.DO_NOTHING,
        verbose_name="Menu",
        help_text="Menu",
        blank=True, null=True
    )
    url = models.TextField(
        verbose_name='URL Document',
        blank=True, null=True
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
