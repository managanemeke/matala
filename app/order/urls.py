from django.urls import path
from . import views


urlpatterns = [
    path('', views.order, name="order"),
    path('order_search/', views.order_search, name="order_search"),
]