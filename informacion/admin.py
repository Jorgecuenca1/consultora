from django.contrib import admin

# Register your models here.
from .models import Pais, Region, City, Profile, TypeDocument,Redsocial,Contacto,Habilidad,Informacion,Comentario,Producto,Stakeholder,Solucion,Productosdelcarro,CarShop
from import_export.admin import ImportExportModelAdmin


@admin.register(Pais)

class PaisAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)
    fieldsets = (
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ('name',)
        }),
    )
    suit_form_tabs = (
        ('general', 'Nuevo país'),
    )


@admin.register(Region)
class RegionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_filter = ('name', )
    search_fields = ('name',)


@admin.register(City)
class CityAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_filter = ('name', )
    search_fields = ('name',)
    fieldsets = (
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ('name','region')
        }),
    )
    suit_form_tabs = (
        ('general', 'Nuevo municipio'),
    )

@admin.register(Profile)
class ProfileAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id',)
    list_filter = ('id', )
    search_fields = ('id',)
@admin.register(TypeDocument)
class TypeDocumentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id',)
    list_filter = ('id', )
    search_fields = ('id',)
@admin.register(Redsocial)
class RedsocialAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id',)
    list_filter = ('id', )
    search_fields = ('id',)
@admin.register(Contacto)
class ContactoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id',)
    list_filter = ('id', )
    search_fields = ('id',)
@admin.register(Habilidad)
class HabilidadAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id',)
    list_filter = ('id', )
    search_fields = ('id',)
@admin.register(Informacion)
class InformacionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id',)
    list_filter = ('id', )
    search_fields = ('id',)
@admin.register(Comentario)
class ComentarioAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id',)
    list_filter = ('id', )
    search_fields = ('id',)
@admin.register(Producto)
class ProductoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id',)
    list_filter = ('id', )
    search_fields = ('id',)
@admin.register(Stakeholder)
class StakeholderAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id',)
    list_filter = ('id', )
    search_fields = ('id',)
@admin.register(Solucion)
class SolucionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id',)
    list_filter = ('id', )
    search_fields = ('id',)
@admin.register(Productosdelcarro)
class ProductosdelcarroAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id',)
    list_filter = ('id', )
    search_fields = ('id',)
@admin.register(CarShop)
class CarShopAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id',)
    list_filter = ('id', )
    search_fields = ('id',)