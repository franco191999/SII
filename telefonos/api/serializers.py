from rest_framework.serializers import ModelSerializer
from telefonos import models

#Serializador para el manejo de las Pizarras
class Pizarra_ListSerializer(ModelSerializer):
    class Meta:
        model= models.Pizarra
        fields='__all__'

#Serializador para el manejo de los telefonos fijos
class Telefonos_Fijos_ListSerializer(ModelSerializer):
    class Meta:
        model= models.Telefono_Fijo
        fields='__all__'

#Serializador para el manejo de las extenciones
class Extenciones_ListSerializer(ModelSerializer):
    class Meta:
        model= models.Extencion
        fields='__all__'

