from rest_framework.serializers import ModelSerializer, DateTimeField
from rest_framework import serializers

from rrhh.models import Trabajador, Perfil, Nom_Cargo_Trabajador, Nom_Titulo_Trabajador, Nom_Habilidad_Trabajador, Userlog, maquina, registromaquina
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

###Serializadores para los elementos de rrhh que no intervienen en la creacion de un trabajador###
#Serializador para el manejo de las habilidades de los trabajadores
class Habilidad_TrabajadorListSerializer(ModelSerializer):
    class Meta:
        model= Nom_Habilidad_Trabajador
        fields='__all__'

class Habilidad_TrabajadorPutPostSerializer(ModelSerializer):
    class Meta:
        model= Nom_Habilidad_Trabajador
        fields=['habilidad','descripcion']

#Serializador para el manejo del cambio de contraseñas de los usuarios
class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


#Serializador para el manejo de los UserLogs de los trabajadores
class UserLogListSerializer(ModelSerializer):
    class Meta:
        model= Userlog
        fields='__all__'

#Serializador para el manejo de los token life
class tokenlifeListSerializer(ModelSerializer):
    class Meta:
        model= Token
        fields='__all__'

class tokenlifePutPostSerializer(serializers.Serializer):
    #key=serializers.CharField()
    #user=serializers.IntegerField(read_only=True)
    created=serializers.DateTimeField()
    
    def create(self, validated_data):
        return Token.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.key= validated_data.get('key',instance.key)
        instance.user= validated_data.get('user',instance.user)
        instance.created= validated_data.get('created',instance.created)
        instance.save()
        return instance
    
    

#Serializador para el manejo de las maquinas de los trabajadores
class MaquinaListSerializer(ModelSerializer):
    class Meta:
        model= maquina
        fields='__all__'
        

class MaquinaPutPostSerializer(ModelSerializer):
    class Meta:
        model= maquina
        fields=['pc','ip']

#Serializador para el manejo de los registros de  las maquinas de los trabajadores
class Registro_MaquinaListSerializer(ModelSerializer):
    class Meta:
        model= registromaquina
        fields='__all__'

class Registro_MaquinaPutPostSerializer(ModelSerializer):
    class Meta:
        model= registromaquina
        fields=['pc','estado']

###Serializadores para los elementos que intervienen en la creacion de un trabajador###
#Serializadores para el manejo de Trabajadores
class TrabajadorListSerializer(ModelSerializer):
    class Meta:
        model= Trabajador
        fields='__all__'

class TrabajadorPutPostSerializer(ModelSerializer):
    class Meta:
        model= Trabajador
        fields=['nombre','imagen','carne','correo','direccion','graduado','telefono','estado','municipio','titulo','plaza_ocupa','cargo']


#Serializadores para el manejo de Usuarios
class UserListSerializer(ModelSerializer):
    class Meta:
        model= User
        fields='__all__'

class UserPutPostSerializer(ModelSerializer):
    class Meta:
        model= User
        fields=['password','is_superuser','username','first_name','last_name','email','is_staff','is_active','groups','user_permissions']

#Serializadores para el manejo de Perfiles
class PerfilListSerializer(ModelSerializer):
    class Meta:
        model= Perfil
        fields='__all__'

class PerfilPutPostSerializer(ModelSerializer):
    class Meta:
        model= Perfil
        fields=['user','trabajador']

#Serializadores para el manejo del cargo de los trabajadores
class Cargo_TrabajadorListSerializer(ModelSerializer):
    class Meta:
        model= Nom_Cargo_Trabajador
        fields='__all__'

class Cargo_TrabajadorPutPostSerializer(ModelSerializer):
    class Meta:
        model= Nom_Cargo_Trabajador
        fields=['cargo','resposabilidad']

#Serializadores para el manejo del titulo de los trabajadores
class Titulo_TrabajadorListSerializer(ModelSerializer):
    class Meta:
        model= Nom_Titulo_Trabajador
        fields='__all__'

class Titulo_TrabajadorPutPostSerializer(ModelSerializer):
    class Meta:
        model= Nom_Titulo_Trabajador
        fields=['titulo','especialidad']

