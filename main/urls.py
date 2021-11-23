from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.home, name='about'),
    path('verkopen', views.verkopen, name='verkopen')
]
