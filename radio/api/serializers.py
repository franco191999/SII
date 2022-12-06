from rest_framework.serializers import ModelSerializer
from radio import models

#Serializador para el manejo de las unidades de radio
class unidad_radio_ListSerializer(ModelSerializer):
    class Meta:
        model= models.unidad_radio
        fields='__all__'

#Serializador para el manejo de las marcas de radio
class nombre_marca_ListSerializer(ModelSerializer):
    class Meta:
        model= models.nom_marca
        fields='__all__'

#Serializador para el manejo de las unidades de radio
class unidad_radio_ListSerializer(ModelSerializer):
    class Meta:
        model= models.unidad_radio
        fields='__all__'
#Serializador para el manejo de los moviles
class movil_ListSerializer(ModelSerializer):
    class Meta:
        model= models.movil
        fields='__all__'

#Serializador para el manejo de las estaciones fijas
class Estaciones_fijas_ListSerializer(ModelSerializer):
    class Meta:
        model= models.estaciones_fijas
        fields='__all__'

#Serializador para el manejo de las estaciones moviles
class estaciones_moviles_ListSerializer(ModelSerializer):
    class Meta:
        model= models.estaciones_movil
        fields='__all__'
#Serializador para el manejo de las estaciones portatiles
class estaciones_portatiles_ListSerializer(ModelSerializer):
    class Meta:
        model= models.estaciones_portatiles
        fields='__all__'
#Serializador para el manejo de las estaciones repetidoras
class estaciones_repetidoras_ListSerializer(ModelSerializer):
    class Meta:
        model= models.estaciones_repetidoras
        fields='__all__'