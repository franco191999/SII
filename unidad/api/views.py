from urllib import request

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics

from unidad import models as unidad

from unidad.api import serializers


##Elementos de unidad necesarios para el funcionamiento de los trabajadores##

# Tipo de plaza del departamento
@api_view(['GET','POST'])
def Tipo_Plaza_List(request):
   
    if request.method =='GET':
        tipo_plaza= unidad.Nom_Tipo_Plaza.objects.all()
        serializer= serializers.Tipo_PlazaListSerializer(tipo_plaza,many=True)
        return Response(serializer.data)
   
    elif request.method =='POST':
        serializer= serializers.Tipo_PlazaPutPostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','Delete'])
def Tipo_Plaza_detail(request, pk):
    try:
        tipo_plaza=unidad.Nom_Tipo_Plaza.objects.get(pk=pk)
    except unidad.Nom_Tipo_Plaza.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method== 'GET':
        serializer= serializers.Tipo_PlazaListSerializer(tipo_plaza)
        return Response(serializer.data)

    elif request.method == 'PUT':
       serializer= serializers.Tipo_PlazaPutPostSerializer(tipo_plaza, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method== 'DELETE':
        tipo_plaza.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


# Nombre de plaza de departamento

@api_view(['GET','POST'])
def Nombre_Plaza_List(request):
   
    if request.method =='GET':
        nombre_plaza= unidad.Nom_Plaza.objects.all()
        serializer= serializers.Nombre_PlazaListSerializer(nombre_plaza,many=True)
        return Response(serializer.data)
   
    elif request.method =='POST':
        serializer= serializers.Nombre_PlazaPutPostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','Delete'])
def Nombre_Plaza_detail(request, pk):
    try:
        nombre_plaza=unidad.Nom_Plaza.objects.get(pk=pk)
    except unidad.Nom_Plaza.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method== 'GET':
        serializer= serializers.Nombre_PlazaListSerializer(nombre_plaza)
        return Response(serializer.data)

    elif request.method == 'PUT':
       serializer= serializers.Nombre_PlazaPutPostSerializer(nombre_plaza, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method== 'DELETE':
        nombre_plaza.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

# Nombre de tipo de unidad organizativa

@api_view(['GET','POST'])
def Tipo_Unidad_Org_List(request):
   
    if request.method =='GET':
        tipo_unidad_org= unidad.tipo_unidad_organizativa.objects.all()
        serializer= serializers.Tipo_Unidad_OrgListSerializer(tipo_unidad_org,many=True)
        return Response(serializer.data)
   
    elif request.method =='POST':
        serializer= serializers.Tipo_Unidad_OrgPutPostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','Delete'])
def Tipo_Unidad_Org_detail(request, pk):
    try:
        tipo_unidad_org=unidad.tipo_unidad_organizativa.objects.get(pk=pk)
    except unidad.tipo_unidad_organizativa.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method== 'GET':
        serializer= serializers.Tipo_Unidad_OrgListSerializer(tipo_unidad_org)
        return Response(serializer.data)

    elif request.method == 'PUT':
       serializer= serializers.Tipo_Unidad_OrgPutPostSerializer(tipo_unidad_org, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method== 'DELETE':
        tipo_unidad_org.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

# add unidad organizativa

@api_view(['GET','POST'])
def Unidad_Org_List(request):
   
    if request.method =='GET':
        unidad_org= unidad.unidad_organizativa.objects.all()
        serializer= serializers.Unidad_OrgListSerializer(unidad_org,many=True)
        return Response(serializer.data)
   
    elif request.method =='POST':
        serializer= serializers.Unidad_OrgPutPostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','Delete'])
def Unidad_Org_detail(request, pk):
    try:
        unidad_org=unidad.unidad_organizativa.objects.get(pk=pk)
    except unidad.unidad_organizativa.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method== 'GET':
        serializer= serializers.Unidad_OrgListSerializer(unidad_org)
        return Response(serializer.data)

    elif request.method == 'PUT':
       serializer= serializers.Unidad_OrgPutPostSerializer(unidad_org, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method== 'DELETE':
        unidad_org.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

# Provincia

@api_view(['GET','POST'])
def Provincia_List(request):
   
    if request.method =='GET':
        provincia= unidad.Nom_Provincia.objects.all()
        serializer= serializers.ProvinciaListSerializer(provincia,many=True)
        return Response(serializer.data)
   
    elif request.method =='POST':
        serializer= serializers.ProvinciaPutPostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','Delete'])
def Provincia_detail(request, pk):
    try:
        provincia=unidad.Nom_Provincia.objects.get(pk=pk)
    except unidad.Nom_Provincia.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method== 'GET':
        serializer= serializers.ProvinciaListSerializer(provincia)
        return Response(serializer.data)

    elif request.method == 'PUT':
       serializer= serializers.ProvinciaPutPostSerializer(provincia, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method== 'DELETE':
        provincia.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

# Municipio

@api_view(['GET','POST'])
def Municipio_List(request):
   
    if request.method =='GET':
        municipio= unidad.Nom_Municipio.objects.all()
        serializer= serializers.MunicipioListSerializer(municipio,many=True)
        return Response(serializer.data)
   
    elif request.method =='POST':
        serializer= serializers.MunicipioPutPostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','Delete'])
def Municipio_detail(request, pk):
    try:
        municipio=unidad.Nom_Municipio.objects.get(pk=pk)
    except unidad.Nom_Municipio.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method== 'GET':
        serializer= serializers.MunicipioListSerializer(municipio)
        return Response(serializer.data)

    elif request.method == 'PUT':
       serializer= serializers.MunicipioPutPostSerializer(municipio, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method== 'DELETE':
        municipio.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

# Nombre del tipo de unidad

@api_view(['GET','POST'])
def Tipo_Unidad_List(request):
   
    if request.method =='GET':
        tipo_unidad= unidad.Nom_Tipo_Unidad.objects.all()
        serializer= serializers.Tipo_UnidadListSerializer(tipo_unidad,many=True)
        return Response(serializer.data)
   
    elif request.method =='POST':
        serializer= serializers.Tipo_UnidadPutPostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','Delete'])
def Tipo_Unidad_detail(request, pk):
    try:
        tipo_unidad=unidad.Nom_Tipo_Unidad.objects.get(pk=pk)
    except unidad.Nom_Tipo_Unidad.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method== 'GET':
        serializer= serializers.Tipo_UnidadListSerializer(tipo_unidad)
        return Response(serializer.data)

    elif request.method == 'PUT':
       serializer= serializers.Tipo_UnidadPutPostSerializer(tipo_unidad, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method== 'DELETE':
        tipo_unidad.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

# Perfil de la unidad

@api_view(['GET','POST'])
def Perfil_Unidad_List(request):
   
    if request.method =='GET':
        perfil_unidad= unidad.Nom_Perfil_Unidad.objects.all()
        serializer= serializers.Perfil_UnidadListSerializer(perfil_unidad,many=True)
        return Response(serializer.data)
   
    elif request.method =='POST':
        serializer= serializers.Perfil_UnidadPutPostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','Delete'])
def Perfil_Unidad_detail(request, pk):
    try:
        perfil_unidad=unidad.Nom_Perfil_Unidad.objects.get(pk=pk)
    except unidad.Nom_Perfil_Unidad.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method== 'GET':
        serializer= serializers.Perfil_UnidadListSerializer(perfil_unidad)
        return Response(serializer.data)

    elif request.method == 'PUT':
       serializer= serializers.Perfil_UnidadPutPostSerializer(perfil_unidad, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method== 'DELETE':
        perfil_unidad.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

# Nivel de la unidad

@api_view(['GET','POST'])
def Nivel_Unidad_List(request):
   
    if request.method =='GET':
        nivel_unidad= unidad.Nom_Nivel_Unidad.objects.all()
        serializer= serializers.Nivel_UnidadListSerializer(nivel_unidad,many=True)
        return Response(serializer.data)
   
    elif request.method =='POST':
        serializer= serializers.Nivel_UnidadPutPostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','Delete'])
def Nivel_Unidad_detail(request, pk):
    try:
        nivel_unidad=unidad.Nom_Nivel_Unidad.objects.get(pk=pk)
    except unidad.Nom_Nivel_Unidad.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method== 'GET':
        serializer= serializers.Nivel_UnidadListSerializer(nivel_unidad)
        return Response(serializer.data)

    elif request.method == 'PUT':
       serializer= serializers.Nivel_UnidadPutPostSerializer(nivel_unidad, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method== 'DELETE':
        nivel_unidad.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

# add Unidad
class UnidadGAPIViewList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin):
    serializer_class= serializers.UnidadListSerializer
    queryset= unidad.Unidad.objects.all()

    lookup_field= 'id'
    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
         return self.list(request)

    def post(self, request):
        return self.create(request)


class UnidadGAPIViewDetail(generics.GenericAPIView, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class= serializers.UnidadListSerializer
    queryset= unidad.Unidad.objects.all()

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


# add Departamento

@api_view(['GET','POST'])
def Departamento_List(request):
   
    if request.method =='GET':
        departamento= unidad.Departamento.objects.all()
        serializer= serializers.DepartamentoListSerializer(departamento,many=True)
        return Response(serializer.data)
   
    elif request.method =='POST':
        serializer= serializers.DepartamentoPutPostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','Delete'])
def Departamento_detail(request, pk):
    try:
        departamento=unidad.Departamento.objects.get(pk=pk)
    except unidad.Departamento.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method== 'GET':
        serializer= serializers.DepartamentoListSerializer(departamento)
        return Response(serializer.data)

    elif request.method == 'PUT':
       serializer= serializers.DepartamentoPutPostSerializer(departamento, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method== 'DELETE':
        departamento.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

# add Plaza de Departamento

@api_view(['GET','POST'])
def Plaza_Departamento_List(request):
   
    if request.method =='GET':
        plaza= unidad.Plaza_Departamento.objects.all()
        serializer= serializers.Plaza_DepartamentoListSerializer(plaza,many=True)
        return Response(serializer.data)
   
    elif request.method =='POST':
        serializer= serializers.Plaza_DepartamentoPutPostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','Delete'])
def Plaza_Departamento_detail(request, pk):
    try:
        plaza=unidad.Plaza_Departamento.objects.get(pk=pk)
    except unidad.Plaza_Departamento.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method== 'GET':
        serializer= serializers.Plaza_DepartamentoListSerializer(plaza)
        return Response(serializer.data)

    elif request.method == 'PUT':
       serializer= serializers.Plaza_DepartamentoPutPostSerializer(plaza, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method== 'DELETE':
        plaza.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)