from rest_framework.serializers import ModelSerializer
from galeria import models

#Serializador para el manejo de las categorias de galeria
class Categoria_GaleriaListSerializer(ModelSerializer):
    class Meta:
        model= models.categorias
        fields='__all__'

class Categoria_GaleriaPutPostSerializer(ModelSerializer):
    class Meta:
        model= models.categorias
        fields=['categoria','descripcion','activo']



#Serializador para el manejo de las imagenes
class ImagenesListSerializer(ModelSerializer):
    class Meta:
        model= models.imagenes
        fields='__all__'

class ImagenesPutPostSerializer(ModelSerializer):
    class Meta:
        model= models.imagenes
        fields=['unidad','categoria','titulo','descripcion','imagen','estado']
        
