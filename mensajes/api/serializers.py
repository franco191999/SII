from rest_framework.serializers import ModelSerializer
from mensajes import models

#Serializador para el manejo de las categorias de mensajes
class Categoria_MensajeListSerializer(ModelSerializer):
    class Meta:
        model= models.categoria
        fields='__all__'

class Categoria_MensajePutPostSerializer(ModelSerializer):
    class Meta:
        model= models.categoria
        fields=['categoria','descripcion','estado']



#Serializador para el manejo de los mensajes
class MensajeListSerializer(ModelSerializer):
    class Meta:
        model= models.mensaje
        fields='__all__'
        

class MensajePutPostSerializer(ModelSerializer):
    class Meta:
        model= models.mensaje
        fields=['categoria','asunto','texto','respuesta','estado','activo','ip','remitente','destinatario']
        read_only_fields = ['ip']

#Serializador para el manejode de eliminar destinatario
class Eliminar_DestinatarioListSerializer(ModelSerializer):
    class Meta:
        model= models.eliminar_destinatario
        fields='__all__'

class Eliminar_DestinatarioPutPostSerializer(ModelSerializer):
    class Meta:
        model= models.eliminar_destinatario
        fields=['mensaje','trabajador','eliminado']

#Serializadores para el manejo del mensaje leido
class Mensaje_LeidoListSerializer(ModelSerializer):
    class Meta:
        model= models.mensaje_leido
        fields='__all__'

class Mensaje_LeidoPutPostSerializer(ModelSerializer):
    class Meta:
        model= models.mensaje_leido
        fields=['mensaje','trabajador']


