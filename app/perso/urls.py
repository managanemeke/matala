from django.urls import path
from . import views


urlpatterns = [
    path('', views.perso, name="perso"),
]