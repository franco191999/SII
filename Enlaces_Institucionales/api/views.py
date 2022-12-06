from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from Enlaces_Institucionales import models
from Enlaces_Institucionales.api import serializers

#elementos para el manejo de las categorias de los mensajes
@api_view(['GET','POST'])

def Enlace_List(request):
   
    if request.method =='GET':
        enlaces=models.Enlaces_Institucionales.objects.all()
        serializer= serializers.EnlaceListSerializer(enlaces,many=True)
        return Response(serializer.data)
   
    elif request.method =='POST':
        serializer= serializers.EnlacePutPostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET','PUT','Delete'])

def Enlace_detail(request, pk):
    try:
        enlaces= models.Enlaces_Institucionales.objects.get(pk=pk)
    except  models.Enlaces_Institucionales.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method== 'GET':
        serializer= serializers.EnlaceListSerializer(enlaces)
        return Response(serializer.data)

    elif request.method == 'PUT':
       serializer= serializers.EnlacePutPostSerializer(enlaces, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method== 'DELETE':
        enlaces.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
