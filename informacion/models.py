from django.db import models
from django.contrib.auth.models import User
SEX_CHOICES = (
        ('F', 'Femenino',),
        ('M', 'Masculino',),
        ('O', 'Otro',),
    )
CHOICES = (
        ('SI', 'SI',),
        ('NO', 'NO',),
    )
ESTADO_CHOICES = (
        ('PAGO', 'PAGO',),
        ('NOPAGO', 'NOPAGO',),

    )
SERVICE_CHOICES = (
        ('Solucion', 'Solucion',),
        ('Servicio', 'Servicio',),

    )
TIPO_CHOICES = (
        ('Persona Natural', 'Persona Natural',),
        ('Persona Juridica', 'Persona Juridica',),

    )
class Pais(models.Model):
    name = models.CharField(verbose_name='Nombre del país', max_length=24)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Paises'

    def __str__(self):
        return self.name



class Region(models.Model):
    name = models.CharField(verbose_name='Nombre del departamento', max_length=54)
    pais = models.ForeignKey(Pais,on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return '{} '.format(self.name)


class City(models.Model):
    name = models.CharField(verbose_name='Nombre municipio', max_length=24)
    region = models.ForeignKey(Region, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'

    def __str__(self):
        return '{} '.format( self.name)

    def save(self, *args, **kwargs):
        super(City, self).save(*args, **kwargs)
class TypeDocument(models.Model):
    name = models.CharField(max_length=30, blank=True, verbose_name='Tipo de documento')
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo de documento'
        verbose_name_plural = 'TIpo de documentos'
class Redsocial(models.Model):
    imagen = models.ImageField(verbose_name='Imagen', null=True, blank=True)
    name = models.CharField(verbose_name='Nombre', max_length=254, null=True, blank=True)
    url = models.CharField(verbose_name='Url', max_length=254, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Red social'
        verbose_name_plural = 'Redes sociales'
class Contacto(models.Model):
    direccion = models.CharField(verbose_name='Direccion', max_length=254, null=True, blank=True)
    redsocial = models.ManyToManyField(Redsocial, verbose_name='Redes sociales')
    correo = models.EmailField(verbose_name='Correo', max_length=254, null=True, blank=True)
    numero = models.CharField(verbose_name='numero', max_length=254, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

class Habilidad(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=254, null=True, blank=True)
    descripcion = models.TextField(verbose_name='Descripción', null=True, blank=True)
    imagen = models.ImageField(verbose_name='Imagen', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skill'
class Informacion(models.Model):
    vision = models.CharField(verbose_name='vision', max_length=254,null=True,blank=True)
    mision = models.CharField(verbose_name='mision', max_length=254, null=True, blank=True)
    objetivos = models.TextField(verbose_name='Objetivos', max_length=254, null=True, blank=True)
    descripcion = models.TextField(verbose_name='Descripcion', max_length=254, null=True, blank=True)
    contacto = models.CharField(verbose_name='Contacto', max_length=254, null=True, blank=True)
    logourl = models.ImageField(verbose_name='Logo',null=True,blank=True)
    habilidades = models.ForeignKey(Habilidad, verbose_name='habilidades',
                                     on_delete=models.PROTECT,
                                     blank=True, null=True)
    contacto = models.ForeignKey(Contacto, verbose_name='Contacto',
                               on_delete=models.PROTECT,
                               blank=True, null=True)


    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Información'
        verbose_name_plural = 'Información'
class Comentario(models.Model):
    comentario = models.CharField(verbose_name='Nombre', max_length=254,null=True,blank=True)
    validado = models.CharField(max_length=4, choices=CHOICES,
                            verbose_name='Validado:',
                            null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
class Producto(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=254,null=True,blank=True)
    comentarios = models.ManyToManyField(Comentario, verbose_name='Productos')
    imagen = models.ImageField(verbose_name='Nombre',null=True,blank=True)
    stock = models.CharField(verbose_name='Stock', max_length=254)
    price = models.CharField(verbose_name='Precio ', max_length=254)
    descripcion = models.TextField(verbose_name='Descripción', null=True,blank=True)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
class Stakeholder(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=254, null=True, blank=True)
    descripcion = models.TextField(verbose_name='Descripción', null=True, blank=True)
    imagen = models.ImageField(verbose_name='Nombre', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Stakeholder'
        verbose_name_plural = 'Stakeholders'
class Solucion(models.Model):
    producto = models.ManyToManyField(Producto, verbose_name='Productos')
    tipo = models.CharField(max_length=10, choices=SERVICE_CHOICES,
                                verbose_name='TIpo:',
                                null=True, blank=True)
    stakeholders = models.ForeignKey(Stakeholder, verbose_name='Stakeholders',
                                      on_delete=models.PROTECT,
                                      blank=True, null=True)
    imagen = models.ImageField(verbose_name='Nombre', null=True, blank=True)
    titulo = models.CharField(verbose_name='Titulo', max_length=254, null=True, blank=True)
    descripcion = models.TextField(verbose_name='Descripción', null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.comprada) or ''

    class Meta:
        verbose_name = 'Solución'
        verbose_name_plural = 'Soluciones'

class Productosdelcarro(models.Model):
    producto = models.ManyToManyField(Producto, verbose_name='Productos')
    cantidad = models.IntegerField( verbose_name='cantidad', null=True,
                                blank=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.cantidad) or ''

    class Meta:
        verbose_name = 'productodelcarro'
        verbose_name_plural = 'Productos del carro'

class CarShop(models.Model):
    productodelcarro = models.ManyToManyField(Productosdelcarro, verbose_name='Productos')
    comprada = models.CharField(max_length=10, choices=ESTADO_CHOICES, verbose_name='Comprada', null=True,
                                blank=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.comprada) or ''

    class Meta:
        verbose_name = 'Carro de compra'
        verbose_name_plural = 'Carros de compra'

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, blank=True, null=True)
    car = models.OneToOneField(CarShop,on_delete=models.PROTECT, blank=True, null=True)
    tipo = models.CharField(max_length=100, choices=TIPO_CHOICES,
                            verbose_name='Tipo de Persona:',
                            null=True, blank=True)
    nit = models.CharField(max_length=100, blank=True, verbose_name='Nit', null=True)

    razon_social = models.CharField(max_length=100, blank=True, verbose_name='Razón Social', null=True)
    historialcar = models.ManyToManyField(CarShop, related_name='Historial')
    email = models.EmailField(max_length=200, verbose_name='Correo electronico', blank=True, null=True)
    first_name = models.CharField(max_length=200, verbose_name='Nombres', blank=True)
    last_name = models.CharField(max_length=200, verbose_name='Apellidos', blank=True)
    type_document = models.ForeignKey(TypeDocument, verbose_name='Tipo de documento',
                                      on_delete=models.PROTECT,
                                      blank=True, null=True)
    identification = models.IntegerField( verbose_name='Número de documento', blank=True, null=True)
    sex = models.CharField(max_length=10, choices=SEX_CHOICES, verbose_name='Sexo', null=True, blank=True)
    fecha_nacimiento = models.DateTimeField(auto_now=False, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True)
    pais = models.ForeignKey(Pais, verbose_name='País', on_delete=models.CASCADE, blank=True, null=True)




    adress = models.CharField(verbose_name='Dirección',max_length=100,blank=True, null=True)
    type_house = models.CharField(verbose_name='Apartamento, unidad,edificio..', max_length=100, blank=True, null=True)
    neighbord = models.CharField(verbose_name='Barrio', max_length=100, blank=True,
                                  null=True)

    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
    