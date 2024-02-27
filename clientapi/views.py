from rest_framework import viewsets
from .serializer import serverSerializer
from .models import server
from rest_framework.response import Response
from rest_framework.decorators import action
import psutil

# Create your views here.

#create a viewset for the server model
class serverView(viewsets.ModelViewSet):
    queryset = server.objects.all()
    serializer_class = serverSerializer
    
    @action(detail=False, methods=['get'])
    def obtener_informacion_disco_y_pid(self, request):
        # Obtener información del disco
        disco = psutil.disk_usage('/')
        total = disco.total / (1024 ** 3)
        libre = disco.free / (1024 ** 3)
        utilizado = disco.used / (1024 ** 3)
        
        # Obtener PID del proceso actual
        pid = psutil.Process().pid
        
        # Construir el diccionario de respuesta
        respuesta = {
            "total": total,
            "libre": libre,
            "utilizado": utilizado,
            "pid": pid
        }
        
        return Response(respuesta)
