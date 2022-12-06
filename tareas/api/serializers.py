from rest_framework.serializers import ModelSerializer
from tareas import models

#Serializador para el manejo de las categorias de las tareas
class Categoria_TareaListSerializer(ModelSerializer):
    class Meta:
        model= models.Nom_Categoria_Tarea
        fields='__all__'

class Categoria_TareaPutPostSerializer(ModelSerializer):
    class Meta:
        model= models.Nom_Categoria_Tarea
        fields=['categoria','activo']



#Serializador para el manejo de las clasificaciones de las tareas
class Clasificacion_TareaListSerializer(ModelSerializer):
    class Meta:
        model= models.Nom_Clasificacion_Tarea
        fields='__all__'

class Clasificacion_TareaPutPostSerializer(ModelSerializer):
    class Meta:
        model= models.Nom_Clasificacion_Tarea
        fields=['clasificacion','activo']

#Serializador para el manejode las prioridades de las tareas
class Prioridad_TareaListSerializer(ModelSerializer):
    class Meta:
        model= models.Nom_Prioridad_Tarea
        fields='__all__'

class Prioridad_TareaPutPostSerializer(ModelSerializer):
    class Meta:
        model= models.Nom_Prioridad_Tarea
        fields=['prioridad','activo']

#Serializadores para el manejo del estado de las tareas
class Estado_TareaListSerializer(ModelSerializer):
    class Meta:
        model= models.Nom_Estado_Tarea
        fields='__all__'

class Estado_TareaPutPostSerializer(ModelSerializer):
    class Meta:
        model= models.Nom_Estado_Tarea
        fields=['estado','activo']


#Serializadores para el manejo de las frecuencias de tareas
class Frecuencia_TareaListSerializer(ModelSerializer):
    class Meta:
        model= models.Nom_Frecuencia_Tarea
        fields='__all__'

class Frecuencia_TareaPutPostSerializer(ModelSerializer):
    class Meta:
        model= models.Nom_Frecuencia_Tarea
        fields=['nombre','activo']

#Serializadores para el manejo de las tareas
class TareaListSerializer(ModelSerializer):
    class Meta:
        model= models.Tarea
        fields='__all__'

class TareaPutPostSerializer(ModelSerializer):
    class Meta:
        model= models.Tarea
        fields=['tarea','descripcion','clasificacion','prioridad','estado','categoria','freg','fini','ffin','responsable','participantes','activo']

