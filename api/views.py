from rest_framework import viewsets
from api.models import Assignament, Event
from api.serializers import AssignamentSerializer, EventSerializer
from rest_framework.pagination import LimitOffsetPagination

from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
import requests

class AssignamentViewSet ( viewsets.ModelViewSet ):
    serializer_class = AssignamentSerializer
    queryset = Assignament.objects.all()
    pagination_class = LimitOffsetPagination
    
    @action(detail=True, methods=['patch'])
    def completardatos(self, request: Request, *args, **kwargs):
    #Extrae el ID del cliente enviado en la url
        id =kwargs['pk']
    # Consulta de base de datos el ID solicitado
        assignament = Assignament.objects.get(pk=id)
    #Consuta de la API externa datos según el identificador proporcionado
        response = requests.get("http://localhost:8083/plannings/"+id)

    #En caso de una respuesta satisfactoria de la api extema, se procede a completar los datos
    #en base de datos y se retorna la respuesa al diente
        if response.status_code == 200:
            data = response.json()
            assignament.planning = data['name']
            assignament.save()
# Prepara un serializador para mapear la entidad a JSON
            serializer = AssignamentSerializer(assignament)
# Regresa una respuesta http con la nueva data del cliente
            return Response(serializer.data, content_type="application/json")
        else:
#si hubo un error en la consulta, devolver un mensaje de error
            return Response("Error en la consula a la API externa", status=500)
   
class EventViewSet ( viewsets.ModelViewSet ):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    


#... otras viewset
