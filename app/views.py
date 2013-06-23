#siempre es un HttpResponse
from django.http import HttpResponse

#importamos el "loader" que permite cargar archivos html (desde las plantillas/templates)
#importamos el "context" que es un diccionario de clave => valor para enviar a nuestro archivos html
from django.template import loader, Context

#simplificando el proceso de template/contexto
from django.shortcuts import render_to_response

#importamos nuestro models para trabajar con la vista
from app.models import Datos


def index(request):
	#imprimiendo html en linea
	#return HttpResponse("<h1>Primera vista del index</h1>")
	t = loader.get_template("index.html")
	c = Context({"nombre":"Ignacio Arguello", "title": "Render with loader/context"})
	#retornamos nuestro template con el contexto
	return HttpResponse(t.render(c))

def home(request):
	return render_to_response("index.html", {"nombre":"ignacio Arguello", "title":"Render with render_to_response"})

#trabajando la vista con nuestro modelo
def lista(request):
	#almacenamos los todos los datos que contiene el modelo "se pueden ordenar"
	datos = Datos.objects.all().order_by('-id') #por el ultimo creado
	return render_to_response("listado.html", {"datos":datos})
	