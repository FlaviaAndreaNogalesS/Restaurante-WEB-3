from django.urls import path
from .views import (
    clientes_list, clientes_create, clientes_update, clientes_delete,
    orden_list, orden_create, orden_update, orden_delete,
    plato_list, plato_create, plato_update, plato_delete, mesero_list, mesero_delete, mesero_update, mesero_create,
    mesa_list, mesa_create, mesa_update, mesa_delete
)

from .views.pago_views import orden_pagar
urlpatterns = [

    path('clientes/', clientes_list, name='clientes_list'),
    path('clientes/create/', clientes_create, name='clientes_create'),
    path('clientes/<int:id>/edit/', clientes_update, name='clientes_update'),
    path('clientes/<int:id>/delete/', clientes_delete, name='clientes_delete'),

    path('ordenes/', orden_list, name='orden_list'),
    path('ordenes/create/', orden_create, name='orden_create'),
    path('ordenes/<int:id>/edit/', orden_update, name='orden_update'),
    path('ordenes/<int:id>/delete/', orden_delete, name='orden_delete'),

    path('platos/', plato_list, name='plato_list'),
    path('platos/create/', plato_create, name='plato_create'),
    path('platos/<int:id>/edit/', plato_update, name='plato_update'),
    path('platos/<int:id>/delete/', plato_delete, name='plato_delete'),

    path('meseros/', mesero_list, name='mesero_list'),
    path('meseros/create/', mesero_create, name='mesero_create'),
    path('meseros/<int:id>/edit/', mesero_update, name='mesero_update'),
    path('meseros/<int:id>/delete/', mesero_delete, name='mesero_delete'),

    path('mesas/', mesa_list, name='mesa_list'),
    path('mesas/create/', mesa_create, name='mesa_create'),
    path('mesas/<int:id>/edit/', mesa_update, name='mesa_update'),
    path('mesas/<int:id>/delete/', mesa_delete, name='mesa_delete'),

    path('ordenes/<int:id>/pagar/', orden_pagar, name='orden_pagar'),

]
