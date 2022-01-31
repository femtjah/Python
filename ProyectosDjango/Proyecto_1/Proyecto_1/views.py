from django.http import HttpResponse
import datetime
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

def saludo(request): #Primera Vista
    p1=Persona(" Profesor Manuel", "Díaz")
    #nombre= "Fabio"
    #apellido= "Marin"
    temasdelcurso= ["Plantillas", "Modelos", "Formularios", "Vistas","Despliege"]
    ahora=datetime.datetime.now()
    #doc_externo=open("C:/Users/femtj/Desktop/Des_Tec_Cer/Progr_Python/ProyectosDjango/Proyecto_1/Proyecto_1/platillas/plantilla1.html")
    #plt=Template(doc_externo.read())
    #doc_externo.close()
    # doc_externo=get_template('plantilla1.html')

    #ctx=Context({"nombre_persona": p1.nombre, "apellido_persona": p1.apellido, "momento_actual":ahora,"temas": temasdelcurso})
    # documento=doc_externo.render({"nombre_persona": p1.nombre, "apellido_persona": p1.apellido, "momento_actual":ahora,"temas": temasdelcurso})
    return render(request, "plantilla1.html",{"nombre_persona": p1.nombre, "apellido_persona": p1.apellido, "momento_actual":ahora,"temas": temasdelcurso})

def CursoC(request):
    fecha_actual=datetime.datetime.now()
    return render(request, "CursoC.html", {"dameFecha":fecha_actual})

def CursoCss(request):
    fecha_actual=datetime.datetime.now()
    return render(request, "CursoCss.html", {"dameFecha":fecha_actual})

def despedida(request):
    return HttpResponse('Hasta luego alumnos Django')    


def dameFecha(request):
    fecha_actual=datetime.datetime.now()
    return HttpResponse('Fecha y hora actuales %s'%fecha_actual)    

def calculaEdad(request, edad,agno):
    #edadActual= 18
    periodo=agno-2021
    edadFutura= edad+periodo
    documento='<html><body><h2>En el año %s tendras %s años</h2></body></html>'%(agno,edadFutura)    
    return HttpResponse(documento)
