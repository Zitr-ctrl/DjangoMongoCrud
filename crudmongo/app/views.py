from django.shortcuts import render, redirect, get_object_or_404
from .models_mongo import Producto
from bson import ObjectId

def lista_productos(request):
    productos = Producto.objects()
    return render(request, 'app/lista.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        Producto(
            nombre=request.POST['nombre'],
            descripcion=request.POST['descripcion'],
            stock=int(request.POST['stock'])
        ).save()
        return redirect('lista_productos')
    return render(request, 'app/crear.html')

def editar_producto(request, producto_id):
    producto = Producto.objects(id=ObjectId(producto_id)).first()
    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.descripcion = request.POST['descripcion']
        producto.stock = int(request.POST['stock'])
        producto.save()
        return redirect('lista_productos')
    return render(request, 'app/editar.html', {'producto': producto})

def eliminar_producto(request, producto_id):
    producto = Producto.objects(id=ObjectId(producto_id)).first()
    if producto:
        producto.delete()
    return redirect('lista_productos')
