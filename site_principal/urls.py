from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('reserva/', views.reserva, name='reserva'),
    path('contato/', views.contato, name='contato'),
]
