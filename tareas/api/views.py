from urllib import request

from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from tareas import models
from tareas.api import serializers

#elementos para el manejo de las categorias de tareas
@api_view(['GET','POST'])
def Categoria_Tarea_List(request):
   
    if request.method =='GET':
        categoria=models.Nom_Categoria_Tarea.objects.all()
        serializer= serializers.Categoria_TareaListSerializer(categoria,many=True)
        return Response(serializer.data)
   
    elif request.method =='POST':
        serializer= serializers.Categoria_TareaPutPostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET','PUT','Delete'])
def Categoria_Tarea_detail(request, pk):
    try:
        categoria= models.Nom_Categoria_Tarea.objects.get(pk=pk)
    except  models.Nom_Categoria_Tarea.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method== 'GET':
        serializer= serializers.Categoria_TareaListSerializer(categoria)
        return Response(serializer.data)

    elif request.method == 'PUT':
       serializer= serializers.Categoria_TareaPutPostSerializer(categoria, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method== 'DELETE':
        categoria.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


#elementor para el manejo de  las clasificaciones de las tareas
@api_view(['GET','POST'])
def Clasificacion_Tareas_List(request):
   
    if request.method =='GET':
        clasificacion=  models.Nom_Clasificacion_Tarea.objects.all()
        serializer= serializers.Clasificacion_TareaListSerializer(clasificacion,many=True)
        return Response(serializer.data)
   
    elif request.method =='POST':
        serializer= serializers.Clasificacion_TareaPutPostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','Delete'])
def Clasificacion_Tareas_detail(request, pk):
    try:
        clasificacion= models.Nom_Clasificacion_Tarea.objects.get(pk=pk)
    except  models.Nom_Clasificacion_Tarea.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method== 'GET':
        serializer= serializers.Clasificacion_TareaListSerializer(clasificacion)
        return Response(serializer.data)

    elif request.method == 'PUT':
       serializer= serializers.Clasificacion_TareaPutPostSerializer(clasificacion, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method== 'DELETE':
        clasificacion.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

#elementor para el manejo de las prioridades de las tareas
@api_view(['GET','POST'])
def Prioridad_Tareas_List(request):
   
    if request.method =='GET':
        prioridad=  models.Nom_Prioridad_Tarea.objects.all()
        serializer= serializers.Prioridad_TareaListSerializer(prioridad,many=True)
        return Response(serializer.data)
   
    elif request.method =='POST':
        serializer= serializers.Prioridad_TareaPutPostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','Delete'])
def Prioridad_Tareas_detail(request, pk):
    try:
        prioridad= models.Nom_Prioridad_Tarea.objects.get(pk=pk)
    except  models.Nom_Prioridad_Tarea.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method== 'GET':
        serializer= serializers.Prioridad_TareaListSerializer(prioridad)
        return Response(serializer.data)

    elif request.method == 'PUT':
       serializer= serializers.Prioridad_TareaPutPostSerializer(prioridad, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method== 'DELETE':
        prioridad.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

#elementor para el manejo del estado de las tareas
@api_view(['GET','POST'])
def Estado_Tareas_List(request):
   
    if request.method =='GET':
        estado=  models.Nom_Estado_Tarea.objects.all()
        serializer= serializers.Estado_TareaListSerializer(estado,many=True)
        return Response(serializer.data)
   
    elif request.method =='POST':
        serializer= serializers.Estado_TareaPutPostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','Delete'])
def Estado_Tareas_detail(request, pk):
    try:
        estado= models.Nom_Estado_Tarea.objects.get(pk=pk)
    except  models.Nom_Estado_Tarea.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method== 'GET':
        serializer= serializers.Estado_TareaListSerializer(estado)
        return Response(serializer.data)

    elif request.method == 'PUT':
       serializer= serializers.Estado_TareaPutPostSerializer(estado, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method== 'DELETE':
        estado.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


# elementos para el manejo de las frecuencias de las tareas

@api_view(['GET','POST'])
def Frecuencia_Tareas_List(request):
   
    if request.method =='GET':
        frecuencia=  models.Nom_Frecuencia_Tarea.objects.all()
        serializer= serializers.Frecuencia_TareaListSerializer(frecuencia,many=True)
        return Response(serializer.data)
   
    elif request.method =='POST':
        serializer= serializers.Frecuencia_TareaPutPostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','Delete'])
def Frecuencia_Tareas_detail(request, pk):
    try:
        frecuencia= models.Nom_Frecuencia_Tarea.objects.get(pk=pk)
    except  models.Nom_Frecuencia_Tarea.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method== 'GET':
        serializer= serializers.Frecuencia_TareaListSerializer(frecuencia)
        return Response(serializer.data)

    elif request.method == 'PUT':
       serializer= serializers.Frecuencia_TareaPutPostSerializer(frecuencia, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method== 'DELETE':
        frecuencia.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


#elementos del manejo de las tareas
@api_view(['GET','POST'])
def Tareas_list(request):
   
    if request.method =='GET':
        tareas= models.Tarea.objects.all()
        serializer= serializers.TareaListSerializer(tareas,many=True)
        return Response(serializer.data)

    elif request.method =='POST':
        serializer= serializers.TareaPutPostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    


@api_view(['GET','PUT','Delete'])
def Tareas_detail(request, pk):
    try:
        tareas=models.Tarea.objects.get(pk=pk)
    except models.Tarea.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method== 'GET':
        serializer= serializers.TareaListSerializer(tareas)
        return Response(serializer.data)

    elif request.method == 'PUT':
       serializer= serializers.TareaPutPostSerializer(tareas, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method== 'DELETE':
        tareas.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

