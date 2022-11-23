from .models import Employed, Sede, Information, Objectives, Functions, Coro
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class PatrimonioAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', )
    search_fields = ('id', 'name',  )
    list_filter = ('name',)

class EmployedAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'contact','carge','extension','phone','fax','email', )
    search_fields = ('id', 'name', 'contact','carge','extension','phone','fax','email', )
    list_filter = ('name',)


class SedeAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'type', 'adress','city','phone','fax','email', )
    search_fields = ('id', 'name', 'type', 'adress','city','phone','fax','email',)
    list_filter = ('name',)

class InformationAdmin(ImportExportModelAdmin):
    list_display = ('id', 'titulo', 'descripcion',  )
    search_fields = ('id', 'titulo', 'descripcion', )
    list_filter = ('titulo',)

class MiViAdmin(ImportExportModelAdmin):
    list_display = ('id', 'mision', 'descriptionmision', 'vision', )
    search_fields = ('id', 'mision', 'descriptionmision', 'vision', )
    list_filter = ('mision',)

class ObjectivesAdmin(ImportExportModelAdmin):
    list_display = ('id', 'objetive', )
    search_fields = ('id', 'objetive',)

class FunctionsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'function' )
    search_fields = ('id', 'function' )
    list_filter = ('function',)
class CoroAdmin(ImportExportModelAdmin):
    list_display = ('id', 'coro' )
    search_fields = ('id', 'coro' )
    list_filter = ('coro',)


admin.site.register(Employed, EmployedAdmin),
admin.site.register(Sede, SedeAdmin),
admin.site.register(Information,InformationAdmin),
admin.site.register(Objectives,ObjectivesAdmin),
admin.site.register(Functions,FunctionsAdmin),
admin.site.register(Coro,CoroAdmin),