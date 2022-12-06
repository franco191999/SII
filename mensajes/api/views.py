from urllib import request

from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status

from mensajes import models
from mensajes.api import serializers
from rest_framework.permissions import IsAuthenticated

#elementos para el manejo de las categorias de los mensajes
@api_view(['GET','POST'])

def Categoria_Mensaje_List(request):
   
    if request.method =='GET':
        categorias=models.categoria.objects.all()
        serializer= serializers.Categoria_MensajeListSerializer(categorias,many=True)
        return Response(serializer.data)
   
    elif request.method =='POST':
        serializer= serializers.Categoria_MensajePutPostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET','PUT','Delete'])

def Categoria_Mensaje_detail(request, pk):
    try:
        categorias= models.categoria.objects.get(pk=pk)
    except  models.categoria.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method== 'GET':
        serializer= serializers.Categoria_MensajeListSerializer(categorias)
        return Response(serializer.data)

    elif request.method == 'PUT':
       serializer= serializers.Categoria_MensajePutPostSerializer(categorias, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method== 'DELETE':
        categorias.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


#elementor para el manejo de los mensajes
@api_view(['GET','POST'])

def Mensaje_List(request):
   
    if request.method =='GET':
        mensajes=  models.mensaje.objects.all()
        serializer= serializers.MensajeListSerializer(mensajes,many=True)
        return Response(serializer.data)
   
    elif request.method =='POST':
        serializer= serializers.MensajePutPostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','Delete'])

def Mensaje_detail(request, pk):
    try:
        mensajes= models.mensaje.objects.get(pk=pk)
    except  models.mensaje.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method== 'GET':
        serializer= serializers.MensajeListSerializer(mensajes)
        return Response(serializer.data)

    elif request.method == 'PUT':
       serializer= serializers.MensajePutPostSerializer(mensajes, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method== 'DELETE':
        mensajes.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

#elementor para el manejo de eliminar destinatarios
@api_view(['GET','POST'])
def Eliminar_Destinatario_List(request):
   
    if request.method =='GET':
        eliminar_d=  models.eliminar_destinatario.objects.all()
        serializer= serializers.Eliminar_DestinatarioListSerializer(eliminar_d,many=True)
        return Response(serializer.data)
   
    elif request.method =='POST':
        serializer= serializers.Eliminar_DestinatarioPutPostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','Delete'])
def Eliminar_Destinatario_detail(request, pk):
    try:
        eliminar_d= models.eliminar_destinatario.objects.get(pk=pk)
    except  models.eliminar_destinatario.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method== 'GET':
        serializer= serializers.Eliminar_DestinatarioListSerializer(eliminar_d)
        return Response(serializer.data)

    elif request.method == 'PUT':
       serializer= serializers.Eliminar_DestinatarioPutPostSerializer(eliminar_d, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method== 'DELETE':
        eliminar_d.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

#elementor para el manejo de los mensajes leidos
@api_view(['GET','POST'])

def Mensaje_Leido_List(request):
   
    if request.method =='GET':
        leido=  models.mensaje_leido.objects.all()
        serializer= serializers.Mensaje_LeidoListSerializer(leido,many=True)
        return Response(serializer.data)
   
    elif request.method =='POST':
        serializer= serializers.Mensaje_LeidoPutPostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','Delete'])

def Mensaje_Leido_detail(request, pk):
    try:
        leido= models.mensaje_leido.objects.get(pk=pk)
    except  models.mensaje_leido.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method== 'GET':
        serializer= serializers.Mensaje_LeidoListSerializer(leido)
        return Response(serializer.data)

    elif request.method == 'PUT':
       serializer= serializers.Mensaje_LeidoPutPostSerializer(leido, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method== 'DELETE':
        leido.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)



