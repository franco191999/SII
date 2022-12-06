from rest_framework.serializers import ModelSerializer
from activos import models

#Serializador para el manejo de los articulos
class Articulos_ListSerializer(ModelSerializer):
    class Meta:
        model= models.articulo
        fields='__all__'

#Serializador para el manejo de los grupos
class Grupos_ListSerializer(ModelSerializer):
    class Meta:
        model= models.grupo
        fields='__all__'

#Serializador para el manejo de los submayores
class Submayor_ListSerializer(ModelSerializer):
    class Meta:
        model= models.submayor
        fields='__all__'

#Serializador para el manejo de los subgrupos
class Subgrupos_ListSerializer(ModelSerializer):
    class Meta:
        model= models.subgrupos
        fields='__all__'

#Serializador para el manejo de los activos
class Activos_ListSerializer(ModelSerializer):
    class Meta:
        model= models.activos
        fields='__all__'

#Serializador para el manejo del orden de activos fijos
class Orden_Act_Fijos_ListSerializer(ModelSerializer):
    class Meta:
        model= models.orden_activos_fijos
        fields='__all__'
