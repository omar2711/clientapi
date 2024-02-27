from django.urls import path, include
from rest_framework import routers
from clientapi import views

router = routers.DefaultRouter()
router.register(r'server', views.serverView)

urlpatterns = [
    path('getinfo/', views.serverView.obtener_informacion_disco_y_pid, name='obtener_informacion_disco_y_pid'),

]

