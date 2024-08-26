# from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.paginaPrincipal, name='PaginaPrincipal'),
    path('', views.pagina1, name='pagina1')
]