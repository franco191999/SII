from rest_framework.serializers import ModelSerializer
from finanzas import models

#Serializador para el manejo de las partidas
class Partida_ListSerializer(ModelSerializer):
    class Meta:
        model= models.nom_partida
        fields='__all__'

#Serializador para el manejo del presupuesto
class Presupuesto_ListSerializer(ModelSerializer):
    class Meta:
        model= models.presupuesto
        fields='__all__'

#Serializador para el manejo de los retiros
class Retiros_ListSerializer(ModelSerializer):
    class Meta:
        model= models.retiros
        fields='__all__'

