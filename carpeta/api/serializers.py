from rest_framework.serializers import ModelSerializer
from carpeta import models

#Serializador para el manejo de las categorias de galeria
class Categoria_ListSerializer(ModelSerializer):
    class Meta:
        model= models.Categoria
        fields='__all__'

#Serializador para el manejo de los ficheros
class Ficheros_ListSerializer(ModelSerializer):
    class Meta:
        model= models.Ficheros
        fields='__all__'

#Serializador para el manejo de los Objetivos
class Objetivos_ListSerializer(ModelSerializer):
    class Meta:
        model= models.Objetivo
        fields='__all__'

#Serializador para el manejo de los tipos de web
class Tipo_Web_ListSerializer(ModelSerializer):
    class Meta:
        model= models.Tipo_web
        fields='__all__'

#Serializador para el manejo de los anchos de banda
class Ancho_Banda_ListSerializer(ModelSerializer):
    class Meta:
        model= models.Ancho_banda
        fields='__all__'

#Serializador para el manejo de los años de unidad
class Anno_Unidad_ListSerializer(ModelSerializer):
    class Meta:
        model= models.Anno_unidad
        fields='__all__'

#Serializador para el manejo de los Resultados
class Resultados_ListSerializer(ModelSerializer):
    class Meta:
        model= models.Resultados
        fields='__all__'

#Serializador para el manejo de la conectividad
class Conectividad_ListSerializer(ModelSerializer):
    class Meta:
        model= models.Conectividad
        fields='__all__'

#Serializador para el manejo de las paginas web
class P_Web_ListSerializer(ModelSerializer):
    class Meta:
        model= models.P_web
        fields='__all__'

#Serializador para el manejo de los enlaces
class Enlaces_ListSerializer(ModelSerializer):
    class Meta:
        model= models.Enlaces
        fields='__all__'

#Serializador para el manejo de las aplicaciones
class Aplicaciones_ListSerializer(ModelSerializer):
    class Meta:
        model= models.Aplicaciones
        fields='__all__'

#Serializador para el manejo de los Documentos
class Documentos_ListSerializer(ModelSerializer):
    class Meta:
        model= models.Documentos
        fields='__all__'