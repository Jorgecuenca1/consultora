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
path('index-2.html', informacion_views.index2, name='index2'),
path('index-3.html', informacion_views.index3, name='index3'),
path('index-4.html', informacion_views.index4, name='index4'),
path('index-5.html', informacion_views.index5, name='index5'),
path('index-6.html', informacion_views.index6, name='index6'),
path('index-7.html', informacion_views.index7, name='index7'),
path('index-8.html', informacion_views.index8, name='index8'),
path('about.html', informacion_views.about, name='about'),
path('about-element-1.html', informacion_views.about1, name='about1'),
path('about-element-2.html', informacion_views.about2, name='about2'),
path('about-element-3.html', informacion_views.about3, name='about3'),
path('about-element-4.html', informacion_views.about4, name='about4'),
path('about-element-5.html', informacion_views.about5, name='about5'),
path('about-element-6.html', informacion_views.about6, name='about6'),
path('about-element-7.html', informacion_views.about7, name='about7'),
path('advertising-marketing.html', informacion_views.advertising, name='advertising'),
path('blog.html', informacion_views.blog, name='blog'),
path('blog2-.html', informacion_views.blog2, name='blog2'),
path('blog-details.html', informacion_views.blogdetails, name='blogdetails'),
path('chooseus-element-1.html', informacion_views.chooseus1, name='chooseus1'),
path('chooseus-element-2.html', informacion_views.chooseus2, name='chooseus2'),
path('chooseus-element-3.html', informacion_views.chooseus3, name='chooseus3'),
path('chooseus-element-4.html', informacion_views.chooseus4, name='chooseus4'),
path('contact.html', informacion_views.contact, name='contact'),
path('error.html', informacion_views.error, name='error'),
path('faq.html', informacion_views.faq, name='faq'),
path('financials-banking.html', informacion_views.financials, name='financials'),
path('grid.html', informacion_views.grid, name='grid'),
path('grid-list.html', informacion_views.gridlist, name='gridlist'),
path('healthcare-medicine.html', informacion_views.healthcaremedicine, name='healthcaremedicine'),
path('media-entertainment.html', informacion_views.mediaentertainment, name='mediaentertainment'),
path('news-element-1.html', informacion_views.newselement1, name='newselement1'),
path('news-element-2.html', informacion_views.newselement2, name='newselement2'),
path('news-element-3.html', informacion_views.newselement3, name='newselement3'),
path('news-element-4.html', informacion_views.newselement4, name='newselement4'),
path('pricing.html', informacion_views.pricing, name='pricing'),
path('project.html', informacion_views.project, name='project'),
path('project-2.html', informacion_views.project2, name='project2'),
path('project-3.html', informacion_views.project3, name='project3'),
path('project-details.html', informacion_views.projectdetails, name='projectdetails'),
path('service.html', informacion_views.service, name='service'),
path('service-element-1.html', informacion_views.serviceelement1, name='serviceelement1'),
path('service-element-2.html', informacion_views.serviceelement2, name='serviceelement2'),
path('service-element-3.html', informacion_views.serviceelement3, name='serviceelement3'),
path('service-element-4.html', informacion_views.serviceelement4, name='serviceelement4'),
path('service-element-5.html', informacion_views.serviceelement5, name='serviceelement5'),
path('skills-element-1.html', informacion_views.skillselement1, name='skillselement1'),
path('skills-element-2.html', informacion_views.skillselement2, name='skillselement2'),
path('team.html', informacion_views.team, name='team'),
path('team-element-1.html', informacion_views.teamelement1, name='teamelement1'),
path('team-element-2.html', informacion_views.teamelement2, name='teamelement2'),
path('team-element-3.html', informacion_views.teamelement3, name='teamelement3'),
path('team-element-4.html', informacion_views.teamelement4, name='teamelement4'),
path('trasportation-logistics.html', informacion_views.trasportationlogistics, name='trasportationlogistics'),
path('travel-hospitality.html', informacion_views.travelhospitality, name='travelhospitality'),
path('working-element-1.html', informacion_views.workingelement1, name='workingelement1'),
path('working-element-2.html', informacion_views.workingelement2, name='workingelement2'),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
