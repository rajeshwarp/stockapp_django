from django.urls import path

from . import views
from .views import home

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('add_stock', views.add_stock, name='add_stock'),
]
