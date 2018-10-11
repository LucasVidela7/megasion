from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
import pprint
from .models import Categoria, Producto


def index(request):
    categorias = Categoria.objects.all()
    categorias_show = Categoria.objects.all()[:3]
    categorias_hide = Categoria.objects.all()[3:]
    context = {'categorias':categorias,'categorias_show': categorias_show, 'categorias_hide':categorias_hide}
    return render(request, 'backoffice/index.html', context)


def productos(request):
    categorias = Categoria.objects.all()
    width = (int)(99 / len(categorias))

    context = {'categorias': categorias}
    return render(request, 'backoffice/productos.html', context)


def productos_categorias(request, nombre_categoria):
    print(nombre_categoria)
    try:
        id_categoria = Categoria.objects.get(nombre_categoria=nombre_categoria).id
    except Categoria.DoesNotExist:
        id_categoria = None

    productos_return = Producto.objects.filter(categoria_id=id_categoria)

    context = {'productos_categoria': productos_return, 'url_categoria': nombre_categoria}
    return render(request, 'backoffice/productos.html', context)


def detalle_producto(request, nombre_categoria, id_producto):
    try:
        producto = Producto.objects.get(id=id_producto)
    except Producto.DoesNotExist:
        producto = None

    # print(producto.descripcion)
    context = {'producto': producto, 'url_categoria': nombre_categoria,'url_producto': producto.nombre_producto}
    return render(request, 'backoffice/productos.html', context)
