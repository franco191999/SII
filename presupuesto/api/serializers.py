from rest_framework.serializers import ModelSerializer
from presupuesto import models

#Serializador para el manejo del presupuesto de la unidad
class Presupuesto_Unidad_ListSerializer(ModelSerializer):
    class Meta:
        model= models.Presupuesto_Unidad
        fields='__all__'

#Serializador para el manejo del orden de servicios de la unidad
class Orden_Servicio_Unidad_ListSerializer(ModelSerializer):
    class Meta:
        model= models.Orden_Servicio_Unidad
        fields='__all__'
