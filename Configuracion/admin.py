from .models import Pagina, Document, \
    Control, Owner, Place, Restaurant,SubModule,Module, \
    Convocatoria, Image, Transparencia, Normatividad, Planeacion, Presupuesto, Noticia, SubMenu, Menu,Slider
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
import nested_admin
# Register your models here.

class DocumentInline(admin.TabularInline):
    model = Document
class SubMenuInline(admin.TabularInline):
    model = SubMenu
class ImageInline(admin.TabularInline):
    model = Image
class ModuleAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('id', 'name',)
    list_filter = ('name',)

class SliderAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('id', 'name',)
    list_filter = ('name',)
class NoticiaAdmin(ImportExportModelAdmin):
    list_display = ('id', 'titulo',)
    search_fields = ('id', 'titulo',)
    list_filter = ('titulo',)
class MenuAdmin(ImportExportModelAdmin):
    list_display = ('id', 'titulo',)
    search_fields = ('id', 'titulo',)
    list_filter = ('titulo',)
    inlines = [SubMenuInline]

class TransparenciaAdmin(ImportExportModelAdmin):
    list_display = ('id', 'titulo',)
    search_fields = ('id', 'titulo',)
    list_filter = ('titulo',)
    inlines = [SubMenuInline]
class SubModuleAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'module')
    search_fields = ('id', 'name', 'module')
    list_filter = ('id','name')

class ConvocatoriaAdmin(admin.ModelAdmin):
    model = Convocatoria
    inlines = [DocumentInline, ImageInline]

class PaginaAdmin(ImportExportModelAdmin):
    model = Pagina
    inlines = [DocumentInline, ImageInline]

class PlaneacionAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'module')
    search_fields = ('id', 'name', 'module')
    list_filter = ('id','name')
class NormatividadAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'modulo')
    search_fields = ('id', 'name', 'modulo')
    list_filter = ('id','name')

class ControlAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'modulo')
    search_fields = ('id', 'name', 'modulo')
    list_filter = ('id','name')

class PlaneacionAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', )
    search_fields = ('id', 'name',)
    list_filter = ('id','name')
class PresupuestoAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', )
    search_fields = ('id', 'name',)
    list_filter = ('id','name')
admin.site.register(Pagina, PaginaAdmin)
admin.site.register(Convocatoria, ConvocatoriaAdmin)
admin.site.register(Planeacion, PlaneacionAdmin)
admin.site.register(Presupuesto, PresupuestoAdmin)
admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Transparencia, TransparenciaAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Normatividad, NormatividadAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Control,ControlAdmin)
admin.site.register(SubModule, SubModuleAdmin)
admin.site.register(Slider, SliderAdmin)