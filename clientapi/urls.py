from django.urls import path, include
from rest_framework import routers
from clientapi import views
from .views import serverView

router = routers.DefaultRouter()
router.register(r'server', views.serverView)

urlpatterns = [
    path('', include(router.urls)),
    path('getinfo/', serverView.as_view({'get': 'obtener_informacion_disco_y_pid'}), name='obtener_informacion_disco_y_pid'),
]


