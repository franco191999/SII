from rest_framework import mixins
from rest_framework import generics

from presupuesto import models
from presupuesto.api import serializers


# para el manejo del presupuesto de la unidad
class Presupuesto_UnidadGAPIViewList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin):
    serializer_class= serializers.Presupuesto_Unidad_ListSerializer
    queryset= models.Presupuesto_Unidad.objects.all()

    lookup_field= 'id'
    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
         return self.list(request)

    def post(self, request):
        return self.create(request)


class Presupuesto_UnidadGAPIViewDetail(generics.GenericAPIView, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class= serializers.Presupuesto_Unidad_ListSerializer
    queryset= models.Presupuesto_Unidad.objects.all()

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

# para el manejo del orden de servicios de la unidad
class Orden_Servicio_UnidadGAPIViewList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin):
    serializer_class= serializers.Orden_Servicio_Unidad_ListSerializer
    queryset= models.Orden_Servicio_Unidad.objects.all()

    lookup_field= 'id'
    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
         return self.list(request)

    def post(self, request):
        return self.create(request)


class Orden_Servicio_UnidadGAPIViewDetail(generics.GenericAPIView, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class= serializers.Orden_Servicio_Unidad_ListSerializer
    queryset= models.Orden_Servicio_Unidad.objects.all()

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
