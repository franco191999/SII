from rest_framework.serializers import ModelSerializer
from Enlaces_Institucionales import models

#Serializador para el manejo de las categorias de mensajes
class EnlaceListSerializer(ModelSerializer):
    class Meta:
        model= models.Enlaces_Institucionales
        fields='__all__'

class EnlacePutPostSerializer(ModelSerializer):
    class Meta:
        model= models.Enlaces_Institucionales
        fields=['institucion','municipio','numero_servicio','ip_lan','ip_wan','velocidad','observaciones']
