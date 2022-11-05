"""consultora URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from informacion import views as informacion_views
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', informacion_views.index, name='index'),
    path('about', informacion_views.about1, name='about1'),
path('about2', informacion_views.about2, name='about2'),
path('about3', informacion_views.about3, name='about3'),
path('about4', informacion_views.about4, name='about4'),
path('about5', informacion_views.about5, name='about5'),
path('about6', informacion_views.about6, name='about6'),
path('about7', informacion_views.about7, name='about7'),
path('advertising', informacion_views.advertising, name='advertising'),
path('blog', informacion_views.blog, name='blog'),
path('blog2', informacion_views.blog2, name='blog2'),
path('blogdetails', informacion_views.blogdetails, name='blogdetails'),
path('chooseus1', informacion_views.chooseus1, name='chooseus1'),
path('chooseus2', informacion_views.chooseus2, name='chooseus2'),
path('chooseus3', informacion_views.chooseus3, name='chooseus3'),
path('chooseus4', informacion_views.chooseus4, name='chooseus4'),
path('contact', informacion_views.contact, name='contact'),
path('error', informacion_views.error, name='error'),
path('faq', informacion_views.faq, name='faq'),
path('financials', informacion_views.financials, name='financials'),
path('grid', informacion_views.grid, name='grid'),
path('gridlist', informacion_views.gridlist, name='gridlist'),
path('healthcaremedicine', informacion_views.healthcaremedicine, name='healthcaremedicine'),
path('mediaentertainment', informacion_views.mediaentertainment, name='mediaentertainment'),
path('newselement1', informacion_views.newselement1, name='newselement1'),
path('newselement2', informacion_views.newselement2, name='newselement2'),
path('newselement3', informacion_views.newselement3, name='newselement3'),
path('newselement4', informacion_views.newselement4, name='newselement4'),
path('pricing', informacion_views.pricing, name='pricing'),
path('project', informacion_views.project, name='project'),
path('project2', informacion_views.project2, name='project2'),
path('project3', informacion_views.project3, name='project3'),
path('projectdetails', informacion_views.projectdetails, name='projectdetails'),
path('service', informacion_views.service, name='service'),
path('serviceelement1', informacion_views.serviceelement1, name='serviceelement1'),
path('serviceelement2', informacion_views.serviceelement2, name='serviceelement2'),
path('serviceelement3', informacion_views.serviceelement3, name='serviceelement3'),
path('serviceelement4', informacion_views.serviceelement4, name='serviceelement4'),
path('serviceelement5', informacion_views.serviceelement5, name='serviceelement5'),
path('skillselement1', informacion_views.skillselement1, name='skillselement1'),
path('skillselement2', informacion_views.skillselement2, name='skillselement2'),
path('team', informacion_views.team, name='team'),
path('teamelement1', informacion_views.teamelement1, name='teamelement1'),
path('teamelement2', informacion_views.teamelement2, name='teamelement2'),
path('teamelement3', informacion_views.teamelement3, name='teamelement3'),
path('teamelement4', informacion_views.teamelement4, name='teamelement4'),
path('trasportationlogistics', informacion_views.trasportationlogistics, name='trasportationlogistics'),
path('travelhospitality', informacion_views.travelhospitality, name='travelhospitality'),
path('workingelement1', informacion_views.workingelement1, name='workingelement1'),
path('workingelement2', informacion_views.workingelement2, name='workingelement2'),
path('teamelement4', informacion_views.teamelement4, name='teamelement4'),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
