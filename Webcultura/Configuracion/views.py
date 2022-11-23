from django.shortcuts import render

from .models import Pagina, Document, Normatividad, Control,Planeacion, Presupuesto, Convocatoria,Menu,SubMenu, Image, Transparencia, Slider


# Create your views here.
def inicio(request):
    menus = Menu.objects.filter().order_by('id')
    submenus = SubMenu.objects.filter().order_by('id')
    sliders = Slider.objects.filter().order_by('id')
    return render(request, 'index.html', {'menus': menus,'submenus': submenus,'sliders': sliders})
def transparencia(request):
    menus = Menu.objects.filter().order_by('id')
    submenus = SubMenu.objects.filter().order_by('id')

    transparencias = Transparencia.objects.filter().order_by('id')
    return render(request, 'transparencia.html', {'menus': menus,'submenus': submenus,'transparencias':transparencias})
def documentacion(request):
    menus = Menu.objects.filter().order_by('id')
    submenus = SubMenu.objects.filter().order_by('id')
    return render(request, 'documentacion.html', {'menus': menus,'submenus': submenus})

def listadoconvocatoria(request):
    convocatoria2022 = Convocatoria.objects.filter(age='2022')
    convocatoria2021 = Convocatoria.objects.filter(age='2021')
    convocatoria2020 = Convocatoria.objects.filter(age='2020')
    convocatoria2019 = Convocatoria.objects.filter(age='2019')
    convocatoria2018 = Convocatoria.objects.filter(age='2018')
    convocatoria2017 = Convocatoria.objects.filter(age='2017')

    return render(request, 'listadoconvocatoria.html', {'convocatoria2022': convocatoria2022,'convocatoria2021': convocatoria2021,
                                                        'convocatoria2020': convocatoria2020,'convocatoria2019': convocatoria2019,
                                                        'convocatoria20218': convocatoria2018,'convocatoria2017': convocatoria2017})
def convocatoria(request,slug):
    convocatorias = Convocatoria.objects.filter(slug=slug)
    convocatoria = Convocatoria.objects.get(slug=slug)
    documentos = Document.objects.filter(convocatoria=convocatoria)
    imagenes = Image.objects.filter(convocatoria=convocatoria)


    return render(request, 'convocatoria.html', {'convocatorias': convocatorias, 'documentos':documentos, 'imagenes':imagenes})
def pagina(request,slug):
    paginas = Pagina.objects.filter(slug=slug)
    pagina = Pagina.objects.get(slug=slug)
    documentos = Document.objects.filter(pagina=pagina)
    imagenes = Image.objects.filter(pagina=pagina)

    return render(request, 'pagina.html', {'paginas': paginas, 'documentos':documentos, 'imagenes':imagenes})
def normatividad(request):
    normatividads = Normatividad.objects.filter(modulo='LEYES')
    decretos = Normatividad.objects.filter(modulo='DECRETOS')
    resoluciones = Normatividad.objects.filter(modulo='RESOLUCIONES')
    ordenanzas = Normatividad.objects.filter(modulo='ORDENANZAS')
    acuerdos = Normatividad.objects.filter(modulo='ACUERDOS')
    codigos = Normatividad.objects.filter(modulo='CODIGOS')
    manuales = Normatividad.objects.filter(modulo='MANUALES')
    politicas = Normatividad.objects.filter(modulo='POLITICAS')


    return render(request, 'normatividad.html', {'normatividads': normatividads,'decretos': decretos,'resoluciones': resoluciones,
                                                 'ordenanzas': ordenanzas,'acuerdos': acuerdos,'codigos': codigos,'manuales': manuales,'politicas': politicas,
                                                 })

def control(request):
    control2022 = Control.objects.filter(age='2022')
    control2021 = Control.objects.filter(age='2021')
    control2020 = Control.objects.filter(age='2020')
    control2019 = Control.objects.filter(age='2019')
    control2018 = Control.objects.filter(age='2018')


    return render(request, 'controlinterno.html', {'control2022': control2022,'control2021': control2021,'control2020': control2020,
                                                 'control2019': control2019,'control2018': control2018,
                                                 })


def presupuesto(request):
    presupuesto2022 = Presupuesto.objects.filter(age='2022')
    presupuesto2021 = Presupuesto.objects.filter(age='2021')
    presupuesto2020 = Presupuesto.objects.filter(age='2020')
    presupuesto2019 = Presupuesto.objects.filter(age='2019')
    presupuesto2018 = Presupuesto.objects.filter(age='2018')


    return render(request, 'presupuesto.html', {'presupuesto2022': presupuesto2022,'presupuesto2021': presupuesto2021,'presupuesto2020': presupuesto2020,
                                                 'presupuesto2019': presupuesto2019,'presupuesto2018': presupuesto2018,
                                                 })

def planeacion(request):
    plan2022 = Planeacion.objects.filter(age='2022')
    plan2021 = Planeacion.objects.filter(age='2021')
    plan2020 = Planeacion.objects.filter(age='2020')
    plan2019 = Planeacion.objects.filter(age='2019')
    plan2018 = Planeacion.objects.filter(age='2018')


    return render(request, 'planeacion.html', {'plan2022': plan2022,'plan2021': plan2021,'plan2020': plan2020,
                                                 'plan2019': plan2019,'plan2018': plan2018,
                                                 })


