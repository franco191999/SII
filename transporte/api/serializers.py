from rest_framework.serializers import ModelSerializer
from transporte import models

#Serializador para el manejo del tipo de transporte
class Tipo_ListSerializer(ModelSerializer):
    class Meta:
        model= models.tipo
        fields='__all__'

#Serializador para el manejo de la marca
class Marca_ListSerializer(ModelSerializer):
    class Meta:
        model= models.marca
        fields='__all__'

#Serializador para el manejo del estado tecnico
class Estado_Tec_ListSerializer(ModelSerializer):
    class Meta:
        model= models.estadotecnico
        fields='__all__'

#Serializador para el manejo del estado operativo
class Estado_Op_ListSerializer(ModelSerializer):
    class Meta:
        model= models.estadooperativo
        fields='__all__'

#Serializador para el manejo del combustible
class Combustible_ListSerializer(ModelSerializer):
    class Meta:
        model= models.combustible
        fields='__all__'

#Serializador para el manejo de los neumaticos
class Neumaticos_ListSerializer(ModelSerializer):
    class Meta:
        model= models.neumatico
        fields='__all__'

#Serializador para el manejo de las baterias
class Baterias_ListSerializer(ModelSerializer):
    class Meta:
        model= models.bateria
        fields='__all__'

#Serializador para el manejo de la demanda
class Demanda_ListSerializer(ModelSerializer):
    class Meta:
        model= models.demanda
        fields='__all__'

#Serializador para el manejo de las funciones
class Funciones_ListSerializer(ModelSerializer):
    class Meta:
        model= models.funcion
        fields='__all__'

#Serializador para el manejo de los parques
class Parques_ListSerializer(ModelSerializer):
    class Meta:
        model= models.parque
        fields='__all__'

