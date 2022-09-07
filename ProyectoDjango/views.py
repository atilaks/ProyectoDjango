from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
from django.template.loader import get_template

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def despedida(request): # Ejemplo de contenido estático
    respuesta = "Hasta luego"

    return HttpResponse(respuesta)

def dame_fecha(request): # Ejemplo de contenido dinámico
    fecha_actual = datetime.now()

    respuesta = """<html>
    <body>
    <h2>
    Fecha y hora actuales %s
    </h2>
    </body>
    </html>""" % fecha_actual

    return HttpResponse(respuesta)

def calcula_edad(request, edad, agno): # Ejemplo de recepción de parámetros
    periodo = agno - 2022
    edadFutura = edad + periodo

    respuesta = "<html><body><h2>En el agno %s tendrás %s agnos" %(agno, edadFutura)

    return HttpResponse(respuesta)

def saludo_plantilla_base(request): # Ejemplo de plantilla
    """
    CREACIÓN DE PLANTILLAS
    1o - Creación de un objeto Template:
        plt=Template(doc_externo.read())
    2o - Creación de contexto:
        ctx=Context()
    3o - Renderizado del objeto Template
        documento=plt.render(ctx)
    """

    doc_externo = open("C:/Users/jaime/Documents/ProyectoDjango/ProyectoDjango/templates/primera_plantilla.html")

    plt = Template(doc_externo.read())

    doc_externo.close()

    ctx = Context()

    respuesta = plt.render(ctx)

    return HttpResponse(respuesta)

def saludo_plantilla_variable(request): # Ejemplo de plantilla con variable   
    """
    Jerarquía u orden de llamada desde una plantilla:
    Diccionario -> Atributo -> Método -> Índice de lista
    """

    p1 = Persona("Jaime", "Franco")
    ahora = datetime.now()
    lista = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]

# Es una forma de optimizar las cargas. Importando el loader y modificando DIRS (settings)
    doc_externo = get_template('plantilla_variable.html')
    respuesta = doc_externo.render({"nombre_persona" : p1.nombre, "apellido_persona": p1.apellido, "momento_actual": ahora, "temas": lista})

    return HttpResponse(respuesta)