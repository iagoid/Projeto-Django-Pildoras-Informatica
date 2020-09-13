from django.urls import path

from . import views


urlpatterns = [

    path("", views.home, name="home"),
    path("tienda/", views.tienda, name="tienda"),
    path("contacto/", views.contacto, name="contacto"),
]