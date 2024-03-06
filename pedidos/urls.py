from django.urls import path
from . import views


urlpatterns = [
    path('', views.pedidos, name='pedidos'),
    path('contiunar_pedido/<int:id>', views.contiunar_pedido, name='contiunar_pedido'),
    path('verificar_pedido/', views.verificar_pedido, name='verificar_pedido'),
]
