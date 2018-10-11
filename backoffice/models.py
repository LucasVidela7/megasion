from django.db import models


# Create your models here.

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=25)
    imagen = models.FileField(upload_to='categorias/')


    def __str__(self):
        return self.nombre_categoria


class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre_producto = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=1000)
    carateristicas = models.TextField(max_length=1000)

    foto_producto_1 = models.ImageField(blank=False)
    foto_producto_2 = models.ImageField(blank=True)
    foto_producto_3 = models.ImageField(blank=True)
    foto_producto_4 = models.ImageField(blank=True)
    foto_producto_5 = models.ImageField(blank=True)

    visitas = models.IntegerField(default=0)

    # visitas.fields['status'].widget.attrs['readonly'] = True # text input

    def __str__(self):
        return "#"+str(self.id)+" | "+self.nombre_producto