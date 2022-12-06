from rest_framework.serializers import ModelSerializer
from inspeccion import models

#Serializador para el manejo del estado de las deficiencias
class Estado_Deficiencia_ListSerializer(ModelSerializer):
    class Meta:
        model= models.Nom_Estado_Deficiencia
        fields='__all__'

#Serializador para el manejo de los Aspectos de deficiencia
class Aspecto_Deficiencia_ListSerializer(ModelSerializer):
    class Meta:
        model= models.Nom_Aspecto_Deficiencia
        fields='__all__'

#Serializador para el manejo de los tipos de Visitas
class Tipo_Visita_ListSerializer(ModelSerializer):
    class Meta:
        model= models.Nom_Tipo_Visita
        fields='__all__'

#Serializador para el manejo de las visitas
class Visitas_ListSerializer(ModelSerializer):
    class Meta:
        model= models.Visita
        fields='__all__'

#Serializador para el manejo de las deficiencias
class Deficiencias_ListSerializer(ModelSerializer):
    class Meta:
        model= models.Deficiencia
        fields='__all__'

#Serializador para el manejo de las deficiencias por tareas
class DeficienciasXtareas_ListSerializer(ModelSerializer):
    class Meta:
        model= models.deficienciasXtareas
        fields='__all__'
