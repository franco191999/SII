from rest_framework.serializers import ModelSerializer
from distribucion import models

#Serializador para el manejo de los tipos de movimientos
class Tipo_Movimiento_ListSerializer(ModelSerializer):
    class Meta:
        model= models.tipomovimiento
        fields='__all__'

#Serializador para el manejo de las mesas
class Mesas_ListSerializer(ModelSerializer):
    class Meta:
        model= models.mesa
        fields='__all__'

#Serializador para el manejo de los pedidos
class Pedidos_ListSerializer(ModelSerializer):
    class Meta:
        model= models.pedido
        fields='__all__'

#Serializador para el manejo de los movimientos
class Movimientos_ListSerializer(ModelSerializer):
    class Meta:
        model= models.movimiento
        fields='__all__'


