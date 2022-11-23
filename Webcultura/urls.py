"""Webcultura URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from Configuracion import views as configuracion_views
from django.urls import path, re_path, include
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', configuracion_views.inicio, name='inicio'),
    path('pagina/normatividad', configuracion_views.normatividad, name='normatividad'),
    path('pagina/controlinterno', configuracion_views.control, name='control'),
    path('pagina/planeacion', configuracion_views.planeacion, name='planeacion'),
    path('convocatoria/<str:slug>', configuracion_views.convocatoria, name='convocatoria'),
    path('pagina/listadoconvocatoria', configuracion_views.listadoconvocatoria, name='listadoconvocatoria'),
path('pagina/transparencia', configuracion_views.transparencia, name='transparencia'),
    path('pagina/documentacion', configuracion_views.documentacion, name='documentacion'),
    path('pagina/presupuesto', configuracion_views.presupuesto, name='presupuesto'),
    path('pagina/<str:slug>', configuracion_views.pagina, name='pagina'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
