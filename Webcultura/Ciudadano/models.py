from django.db import models
from django.core.exceptions import ValidationError

def file_size(value): # add this to some file where you can import it from
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 2 MiB.')

# Create your models here.

BOOLEAN_CHOICES = (
        ('SI', 'SI',),
        ('NO', 'NO',),

    )
class Tiposolicitud(models.Model):
    name = models.CharField(max_length=30, blank=True, verbose_name='Tipo de solicitud')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo de solicitud'
        verbose_name_plural = 'TIpo de solicitud'

class TypeDocument(models.Model):
    name = models.CharField(max_length=30, blank=True, verbose_name='Tipo de documento')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo de documento'
        verbose_name_plural = 'TIpo de documentos'

class Pqrsd(models.Model):
    tiposolicitud = models.ForeignKey(Tiposolicitud, verbose_name='1.Tipo de solicitud', on_delete=models.PROTECT, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, verbose_name='2.Nombre del remitente', null=True)
    last_name = models.CharField(max_length=200, blank=True, verbose_name='3.Apellidos del remitente', null=True)
    type_document = models.ForeignKey(TypeDocument, verbose_name='4.Tipo de documento',
                                      on_delete=models.PROTECT,
                                      blank=True, null=True)
    identification = models.CharField(max_length=30, verbose_name='5.Identificación', blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, verbose_name='6.Municipio', null=True)
    email = models.EmailField(max_length=30, blank=True, verbose_name='7.Correo electrónico', null=True)
    phone = models.CharField(max_length=30, verbose_name='8.Celular', blank=True, null=True)
    asunto = models.CharField(max_length=400, blank=True, verbose_name='9.Asunto ', null=True)
    solicitud = models.TextField(
                                 verbose_name='10.Descripción Solicitud', null=True,
                                 blank=True)
    archivo = models.FileField(verbose_name='11.Archivo adjunto', upload_to='pqrsd/file', blank=True, null=True, validators=[file_size])
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Informe PQRSD'
        verbose_name_plural = 'Informe PQRSD'

class Nivel(models.Model):
    name = models.CharField(max_length=30, blank=True, verbose_name='Nivel')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Nivel'
        verbose_name_plural = 'Nivel'

class EncuestaTransparencia(models.Model):
    encontro = models.CharField(max_length=2, choices=BOOLEAN_CHOICES,
                                   verbose_name='1. Encontró la información que buscaba?:',
                                   null=True,
                                   blank=True)
    noencontro= models.CharField(max_length=100, blank=True, verbose_name='2. Si no la encontró especifique en este espacio ¿qué buscaba?', null=True)
    facil = models.CharField(max_length=2, choices=BOOLEAN_CHOICES,
                                verbose_name='3. ¿Le resultó fácil la ruta de acceso a la información?:',
                                null=True,
                                blank=True)
    nivel = models.ForeignKey(Nivel, verbose_name='4. ¿A nivel general, cómo define la información contenida en la página web?',
                                      on_delete=models.PROTECT,
                                      blank=True, null=True)
    sugerencia = models.CharField(max_length=100, blank=True, verbose_name='5. Si tiene alguna sugerencia escribanos en el siguiente espacio, recuerde que su opinión es muy importante para mejorar nuestro servicio.', null=True)

    def __str__(self):
        return self.sugerencia

    class Meta:
        verbose_name = 'Encuesta de satisfacción'
        verbose_name_plural = 'Encuesta de satisfacción'