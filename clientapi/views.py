from rest_framework import viewsets
from .serializer import serverSerializer
from .models import server
import psutil
from django.http import JsonResponse


# Create your views here.

#create a viewset for the server model
class serverView(viewsets.ModelViewSet):
    queryset = server.objects.all()
    serializer_class = serverSerializer
    
    def obtener_informacion_disco_y_pid(request):
        # Obtener información del disco
        disco = psutil.disk_usage('/')
        espacio_total_gb = disco.total / (1024 ** 3)
        espacio_libre_gb = disco.free / (1024 ** 3)
        espacio_usado_gb = disco.used / (1024 ** 3)
        
        # Obtener PID del proceso actual
        pid_proceso_actual = psutil.Process().pid
        
        # Construir el diccionario de respuesta
        respuesta = {
            "total": espacio_total_gb,
            "libre": espacio_libre_gb,
            "utilizado": espacio_usado_gb,
            "pid": pid_proceso_actual
        }
        
        return JsonResponse(respuesta)

   

