from rest_framework import mixins
from rest_framework import generics

from telefonos import models
from telefonos.api import serializers


# para el manejo de las Pizarras
class PizarraGAPIViewList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin):
    serializer_class= serializers.Pizarra_ListSerializer
    queryset= models.Pizarra.objects.all()

    lookup_field= 'id'
    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
         return self.list(request)

    def post(self, request):
        return self.create(request)


class PizarraGAPIViewDetail(generics.GenericAPIView, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class= serializers.Pizarra_ListSerializer
    queryset= models.Pizarra.objects.all()

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

# para el manejo de los telefonos fijos
class Telefono_FijoGAPIViewList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin):
    serializer_class= serializers.Telefonos_Fijos_ListSerializer
    queryset= models.Telefono_Fijo.objects.all()

    lookup_field= 'id'
    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
         return self.list(request)

    def post(self, request):
        return self.create(request)


class Telefono_FijoGAPIViewDetail(generics.GenericAPIView, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class= serializers.Telefonos_Fijos_ListSerializer
    queryset= models.Telefono_Fijo.objects.all()

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

# para el manejo de las extenciones
class ExtencionGAPIViewList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin):
    serializer_class= serializers.Extenciones_ListSerializer
    queryset= models.Extencion.objects.all()

    lookup_field= 'id'
    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
         return self.list(request)

    def post(self, request):
        return self.create(request)


class ExtencionGAPIViewDetail(generics.GenericAPIView, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class= serializers.Extenciones_ListSerializer
    queryset= models.Extencion.objects.all()

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

