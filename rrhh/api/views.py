from ast import Delete
from urllib import request

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics

from rrhh import models
from rrhh.api import serializers

from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from rrhh.api.Authentication import token_expire_handler, expires_in

#autenticacion
@api_view(['POST'])
@permission_classes([~IsAuthenticated])
def login(request):
    username=request.POST.get('username')
    password=request.POST.get('password')

    
    try:
        user=User.objects.get(username=username)
    except User.DoesNotExist:
        return Response('usuario desconocido')

    pwd_valid=check_password(password,user.password)

    if not pwd_valid:
        return Response('contraseña incorrecta')

    token, _=Token.objects.get_or_create(user=user)
   # token =Token.objects.create(user=user)
    is_expired, token = token_expire_handler(token)
    

    
    return Response({
       'token': token.key,
        'expires_in':expires_in(token),})

#logout
class Logout(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

#Change Password
class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = serializers.ChangePasswordSerializer
    model = User

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Se actualizó correctamente la contraseña',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#elementor para el manejo de los tokenlife
@api_view(['GET','POST'])

def token_life_List(request):
   
    if request.method =='GET':
        tokenlife=  Token.objects.all()
        serializer= serializers.tokenlifeListSerializer(tokenlife,many=True)
        
        return Response(serializer.data)
   
    elif request.method =='POST':
        serializer= serializers.tokenlifePutPostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','Delete'])

def token_life_detail(request, user):
    try:
        tokenlife= Token.objects.get(user=user)
    except  Token.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method== 'GET':
        serializer= serializers.tokenlifeListSerializer(tokenlife)
        return Response(serializer.data)

    elif request.method == 'PUT':
       serializer= serializers.tokenlifePutPostSerializer(tokenlife, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method== 'DELETE':
        tokenlife.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

#elementor para el manejo de los Logs de los trabajadores
@api_view(['GET'])
def UserLog_List(request):

    if request.method =='GET':
        userlog= models.Userlog.objects.all()
        serializer= serializers.UserLogListSerializer(userlog,many=True)

        return Response(serializer.data)
   
    


@api_view(['GET','Delete'])
def UserLog_detail(request, pk):
    try:
        userlog= models.Userlog.objects.get(pk=pk)
    except  models.Userlog.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method== 'GET':
        serializer= serializers.UserLogListSerializer(userlog)
        return Response(serializer.data)

   

    elif request.method== 'DELETE':
        userlog.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


#elementor para el manejo de  habilidad de trabajador
@api_view(['GET','POST'])
def Habilidad_Trabajador_List(request):
   
    if request.method =='GET':
        habilidad_trabajador=  models.Nom_Habilidad_Trabajador.objects.all()
        serializer= serializers.Habilidad_TrabajadorListSerializer(habilidad_trabajador,many=True)
        return Response(serializer.data)
   
    elif request.method =='POST':
        serializer= serializers.Habilidad_TrabajadorPutPostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','Delete'])
def Habilidad_Trabajador_detail(request, pk):
    try:
        habilidad_trabajador= models.Nom_Habilidad_Trabajador.objects.get(pk=pk)
    except  models.Nom_Habilidad_Trabajador.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method== 'GET':
        serializer= serializers.Habilidad_TrabajadorListSerializer(habilidad_trabajador)
        return Response(serializer.data)

    elif request.method == 'PUT':
       serializer= serializers.Habilidad_TrabajadorPutPostSerializer(habilidad_trabajador, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method== 'DELETE':
        habilidad_trabajador.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

#elementor para el manejo de las maquinas de los trabajadores
@api_view(['GET','POST'])
def Maquina_List(request):
   
    if request.method =='GET':
        maquinas=  models.maquina.objects.all()
        serializer= serializers.MaquinaListSerializer(maquinas,many=True)
        return Response(serializer.data)
   
    elif request.method =='POST':
        serializer= serializers.MaquinaPutPostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','Delete'])
def Maquina_detail(request, pk):
    try:
        maquinas= models.maquina.objects.get(pk=pk)
    except  models.maquina.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method== 'GET':
        serializer= serializers.MaquinaListSerializer(maquinas)
        return Response(serializer.data)

    elif request.method == 'PUT':
       serializer= serializers.MaquinaPutPostSerializer(maquinas, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method== 'DELETE':
        maquinas.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

#elementor para el manejo de los registros de las maquinas de los trabajadores
@api_view(['GET','POST'])
def Registro_Maquina_List(request):
   
    if request.method =='GET':
        registro_maquinas=  models.registromaquina.objects.all()
        serializer= serializers.Registro_MaquinaListSerializer(registro_maquinas,many=True)
        return Response(serializer.data)
   
    elif request.method =='POST':
        serializer= serializers.Registro_MaquinaPutPostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','Delete'])
def Registro_Maquina_detail(request, pk):
    try:
        registro_maquinas= models.registromaquina.objects.get(pk=pk)
    except  models.registromaquina.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method== 'GET':
        serializer= serializers.Registro_MaquinaListSerializer(registro_maquinas)
        return Response(serializer.data)

    elif request.method == 'PUT':
       serializer= serializers.Registro_MaquinaPutPostSerializer(registro_maquinas, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method== 'DELETE':
        registro_maquinas.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


###Todo lo necesario para poder crear un trabajador###

# elementos del trabajador en rrhh

class TrabajadorGAPIViewList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin):
    serializer_class= serializers.TrabajadorListSerializer
    
    queryset= models.Trabajador.objects.all()

    lookup_field= 'id'
    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
         return self.list(request)

    def post(self, request):
        return self.create(request)


class TrabajadorGAPIViewDetail(generics.GenericAPIView, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class= serializers.TrabajadorListSerializer
    
    queryset= models.Trabajador.objects.all()

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


#elementos del manejo de usuarios    
@api_view(['GET','POST'])

def User_list(request):
   
    if request.method =='GET':
        usuario= User.objects.all()
        serializer= serializers.UserListSerializer(usuario,many=True)
        return Response(serializer.data)

    elif request.method =='POST':
        serializer= serializers.UserPutPostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    


@api_view(['GET','PUT','Delete'])

def User_detail(request, pk):
    try:
        usuario=User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method== 'GET':
        serializer= serializers.UserListSerializer(usuario)
        return Response(serializer.data)

    elif request.method == 'PUT':
       serializer= serializers.UserPutPostSerializer(usuario, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method== 'DELETE':
        usuario.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

#elementos del manejo de perfiles
@api_view(['GET','POST'])

def Perfil_List(request):
   
    if request.method =='GET':
        trabajador=  models.Perfil.objects.all()
        serializer= serializers.PerfilListSerializer(trabajador,many=True)
        return Response(serializer.data)
   
    elif request.method =='POST':
        serializer= serializers.PerfilListSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','Delete'])

def Perfil_detail(request, pk):
    try:
        perfil= models.Perfil.objects.get(pk=pk)
    except  models.Perfil.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method== 'GET':
        serializer= serializers.PerfilListSerializer(perfil)
        return Response(serializer.data)

    elif request.method == 'PUT':
       serializer= serializers.PerfilPutPostSerializer(perfil, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method== 'DELETE':
        perfil.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

# elementos del cargo del trabajador en rrhh

@api_view(['GET','POST'])
def Cargo_Trabajador_List(request):
   
    if request.method =='GET':
        cargo=  models.Nom_Cargo_Trabajador.objects.all()
        serializer= serializers.Cargo_TrabajadorListSerializer(cargo,many=True)
        return Response(serializer.data)
   
    elif request.method =='POST':
        serializer= serializers.Cargo_TrabajadorPutPostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','Delete'])
def Cargo_Trabajador_detail(request, pk):
    try:
        cargo= models.Nom_Cargo_Trabajador.objects.get(pk=pk)
    except  models.Nom_Cargo_Trabajador.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method== 'GET':
        serializer= serializers.Cargo_TrabajadorListSerializer(cargo)
        return Response(serializer.data)

    elif request.method == 'PUT':
       serializer= serializers.Cargo_TrabajadorPutPostSerializer(cargo, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method== 'DELETE':
        cargo.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

# elementos del Titulo del trabajador en rrhh

@api_view(['GET','POST'])
def Titulo_Trabajador_List(request):
   
    if request.method =='GET':
        titulo=  models.Nom_Titulo_Trabajador.objects.all()
        serializer= serializers.Titulo_TrabajadorListSerializer(titulo,many=True)
        return Response(serializer.data)
   
    elif request.method =='POST':
        serializer= serializers.Titulo_TrabajadorPutPostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','Delete'])
def Titulo_Trabajador_detail(request, pk):
    try:
        titulo= models.Nom_Titulo_Trabajador.objects.get(pk=pk)
    except  models.Nom_Titulo_Trabajador.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method== 'GET':
        serializer= serializers.Titulo_TrabajadorListSerializer(titulo)
        return Response(serializer.data)

    elif request.method == 'PUT':
       serializer= serializers.Titulo_TrabajadorPutPostSerializer(titulo, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method== 'DELETE':
        titulo.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

