from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # ex: /productos/Semáforos/
    path('productos/', views.productos, name='productos'),
    # ex: /productos/Semáforos/
    path('productos/<str:nombre_categoria>/', views.productos_categorias, name='productos_categorias'),
    # ex: /productos/Semáforos/<id>
    path('productos/<str:nombre_categoria>/<int:id_producto>/', views.detalle_producto, name='detalle_producto'),

]
