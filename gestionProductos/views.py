from django.shortcuts import render, get_object_or_404
from .models import Producto, Chollo, Noticia

def home(request):
    context = {}
    noticias = Noticia.objects.all()
    context = {
        'noticias': noticias
    }
    return render(request, "index.html", context)

def contacto(request):
    return render(request, "contacto.html", {})

def about(request):
    return render(request, "about.html", {})

def aviso(request):
    return render(request, "aviso.html", {})
    
def productos(request):
    context = {}
    categoria = request.GET.get("c")
    subcategoria = request.GET.get("s")
    marca = request.GET.get("m")
    producto = request.GET.get("p")

    if categoria:
        mostrar = Producto.objects.filter(categoria=categoria)
    elif subcategoria:
        mostrar = Producto.objects.filter(subcategoria=subcategoria)
    elif marca:
        mostrar = Producto.objects.filter(marca=marca)
    elif producto:
        mostrar = Producto.objects.filter(nombre=producto)
    else:
        mostrar = Producto.objects.all()
    
    context["productos"] = mostrar

    return render(request, "productos.html", context)

def producto(request, slug):
    product = get_object_or_404(Producto, slug=slug)
    context = {
        'producto': product
    }
    return render(request, "producto.html", context)

def ocasion(request):
    context = {}
    producto = request.GET.get("p")
    if producto:
        mostrar=Chollo.objects.filter(nombre=producto)
    else:
        mostrar = Chollo.objects.all()
    context = {
        'chollos': mostrar
    }
    return render(request, "ocasion.html", context)

def chollo(request, slug):
    chollo_mostrar = get_object_or_404(Chollo, slug=slug)
    context = {
        'chollo': chollo_mostrar
    }
    return render(request, "chollo.html", context)