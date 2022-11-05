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
    path('about.html', informacion_views.about1, name='about1'),
path('about2.html', informacion_views.about2, name='about2'),
path('about3.html', informacion_views.about3, name='about3'),
path('about4.html', informacion_views.about4, name='about4'),
path('about5.html', informacion_views.about5, name='about5'),
path('about6.html', informacion_views.about6, name='about6'),
path('about7.html', informacion_views.about7, name='about7'),
path('advertising.html', informacion_views.advertising, name='advertising'),
path('blog.html', informacion_views.blog, name='blog'),
path('blog2.html', informacion_views.blog2, name='blog2'),
path('blogdetails.html', informacion_views.blogdetails, name='blogdetails'),
path('chooseus1.html', informacion_views.chooseus1, name='chooseus1'),
path('chooseus2.html', informacion_views.chooseus2, name='chooseus2'),
path('chooseus3.html', informacion_views.chooseus3, name='chooseus3'),
path('chooseus4.html', informacion_views.chooseus4, name='chooseus4'),
path('contact.html', informacion_views.contact, name='contact'),
path('error.html', informacion_views.error, name='error'),
path('faq.html', informacion_views.faq, name='faq'),
path('financials.html', informacion_views.financials, name='financials'),
path('grid.html', informacion_views.grid, name='grid'),
path('gridlist.html', informacion_views.gridlist, name='gridlist'),
path('healthcaremedicine.html', informacion_views.healthcaremedicine, name='healthcaremedicine'),
path('mediaentertainment.html', informacion_views.mediaentertainment, name='mediaentertainment'),
path('newselement1.html', informacion_views.newselement1, name='newselement1'),
path('newselement2.html', informacion_views.newselement2, name='newselement2'),
path('newselement3.html', informacion_views.newselement3, name='newselement3'),
path('newselement4.html', informacion_views.newselement4, name='newselement4'),
path('pricing.html', informacion_views.pricing, name='pricing'),
path('project.html', informacion_views.project, name='project'),
path('project2.html', informacion_views.project2, name='project2'),
path('project3.html', informacion_views.project3, name='project3'),
path('projectdetails.html', informacion_views.projectdetails, name='projectdetails'),
path('service.html', informacion_views.service, name='service'),
path('serviceelement1.html', informacion_views.serviceelement1, name='serviceelement1'),
path('serviceelement2.html', informacion_views.serviceelement2, name='serviceelement2'),
path('serviceelement3.html', informacion_views.serviceelement3, name='serviceelement3'),
path('serviceelement4.html', informacion_views.serviceelement4, name='serviceelement4'),
path('serviceelement5.html', informacion_views.serviceelement5, name='serviceelement5'),
path('skillselement1.html', informacion_views.skillselement1, name='skillselement1'),
path('skillselement2.html', informacion_views.skillselement2, name='skillselement2'),
path('team.html', informacion_views.team, name='team'),
path('teamelement1.html', informacion_views.teamelement1, name='teamelement1'),
path('teamelement2.html', informacion_views.teamelement2, name='teamelement2'),
path('teamelement3.html', informacion_views.teamelement3, name='teamelement3'),
path('teamelement4.html', informacion_views.teamelement4, name='teamelement4'),
path('trasportationlogistics.html', informacion_views.trasportationlogistics, name='trasportationlogistics'),
path('travelhospitality.html', informacion_views.travelhospitality, name='travelhospitality'),
path('workingelement1.html', informacion_views.workingelement1, name='workingelement1'),
path('workingelement2.html', informacion_views.workingelement2, name='workingelement2'),
path('teamelement4.html', informacion_views.teamelement4, name='teamelement4'),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
