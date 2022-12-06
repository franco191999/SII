from rest_framework import mixins
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.http import HttpResponse

from galeria import models
from galeria.api import serializers

#elementos para el manejo de las categorias de la galeria
@api_view(['GET','POST'])


def Categoria_Galeria_List(request):
   
    if request.method =='GET':
        categoria=models.categorias.objects.all()
        serializer= serializers.Categoria_GaleriaListSerializer(categoria,many=True)
        return Response(serializer.data)
   
    elif request.method =='POST':
        serializer= serializers.Categoria_GaleriaPutPostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET','PUT','Delete'])
def Categoria_Galeria_detail(request, pk):
    try:
        categoria= models.categorias.objects.get(pk=pk)
    except  models.categorias.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method== 'GET':
        serializer= serializers.Categoria_GaleriaListSerializer(categoria)
        return Response(serializer.data)

    elif request.method == 'PUT':
       serializer= serializers.Categoria_GaleriaPutPostSerializer(categoria, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method== 'DELETE':
        categoria.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)




class GaleriaGAPIViewList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin):
    serializer_class= serializers.ImagenesListSerializer
    queryset= models.imagenes.objects.all()

    lookup_field= 'id'
    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
         return self.list(request)

    def post(self, request):
        return self.create(request)


class GaleriaGAPIViewDetail(generics.GenericAPIView, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class= serializers.ImagenesListSerializer
    queryset= models.imagenes.objects.all()

    lookup_field= 'id'
    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
         return self.list(request)

    
    def put(self, request, id=None):
        return self.update(request,id)
    
    def delete(self, request, id):
        return self.destroy(request,id)