from rest_framework.serializers import ModelSerializer

from unidad import models as unidad





#Serializadores para el manejo de los tipos de plaza
class Tipo_PlazaListSerializer(ModelSerializer):
    class Meta:
        model= unidad.Nom_Tipo_Plaza
        fields='__all__'

class Tipo_PlazaPutPostSerializer(ModelSerializer):
    class Meta:
        model= unidad.Nom_Tipo_Plaza
        fields=['tipoplaza']

#Serializadores para el manejo de los nombres de plaza
class Nombre_PlazaListSerializer(ModelSerializer):
    class Meta:
        model= unidad.Nom_Plaza
        fields='__all__'

class Nombre_PlazaPutPostSerializer(ModelSerializer):
    class Meta:
        model= unidad.Nom_Plaza
        fields=['req_formales','salario','activo','plaza']

#Serializadores para el manejo del tipo de unidad organizativa
class Tipo_Unidad_OrgListSerializer(ModelSerializer):
    class Meta:
        model= unidad.tipo_unidad_organizativa
        fields='__all__'

class Tipo_Unidad_OrgPutPostSerializer(ModelSerializer):
    class Meta:
        model= unidad.tipo_unidad_organizativa
        fields=['nombre','activo']

#Serializadores para el manejo de las unidades organizativas
class Unidad_OrgListSerializer(ModelSerializer):
    class Meta:
        model= unidad.unidad_organizativa
        fields='__all__'

class Unidad_OrgPutPostSerializer(ModelSerializer):
    class Meta:
        model= unidad.unidad_organizativa
        fields=['nombre','activo']

#Serializadores para el manejo de las Provincias
class ProvinciaListSerializer(ModelSerializer):
    class Meta:
        model= unidad.Nom_Provincia
        fields='__all__'
class ProvinciaPutPostSerializer(ModelSerializer):
    class Meta:
        model= unidad.Nom_Provincia
        fields=['municipio','activo']

#Serializadores para el manejo de los municipios
class MunicipioListSerializer(ModelSerializer):
    class Meta:
        model= unidad.Nom_Municipio
        fields='__all__'

class MunicipioPutPostSerializer(ModelSerializer):
    class Meta:
        model= unidad.Nom_Municipio
        fields=['codigo','municipio','activo','provincia']

#Serializadores para el manejo de los nombres del tipo de unidad
class Tipo_UnidadListSerializer(ModelSerializer):
    class Meta:
        model= unidad.Nom_Tipo_Unidad
        fields='__all__'

class Tipo_UnidadPutPostSerializer(ModelSerializer):
    class Meta:
        model= unidad.Nom_Tipo_Unidad
        fields=['tipo','activo']

#Serializadores para el manejo de los perfiles de unidad
class Perfil_UnidadListSerializer(ModelSerializer):
    class Meta:
        model= unidad.Nom_Perfil_Unidad
        fields='__all__'

class Perfil_UnidadPutPostSerializer(ModelSerializer):
    class Meta:
        model= unidad.Nom_Perfil_Unidad
        fields=['perfil','activo']

#Serializadores para el manejo del nivel de la unidad
class Nivel_UnidadListSerializer(ModelSerializer):
    class Meta:
        model= unidad.Nom_Nivel_Unidad
        fields='__all__'

class Nivel_UnidadPutPostSerializer(ModelSerializer):
    class Meta:
        model= unidad.Nom_Nivel_Unidad
        fields=['nivel','activo']

#Serializadores para el manejo de las unidades
class UnidadListSerializer(ModelSerializer):
    class Meta:
        model= unidad.Unidad
        fields='__all__'

class UnidadPutPostSerializer(ModelSerializer):
    class Meta:
        model= unidad.Unidad
        fields=['codigo','nombre','direccion','telefono','imagen','activo','municipio','tipo','perfil','nivel','subordinacion']


#Serializadores para el manejo de los departamentos
class DepartamentoListSerializer(ModelSerializer):
    class Meta:
        model= unidad.Departamento
        fields='__all__'

class DepartamentoPutPostSerializer(ModelSerializer):
    class Meta:
        model= unidad.Departamento
        fields=['telefono','activo','tipouorganizativa','nombre','unidad']

#Serializadores para el manejo de las plazas de departamentos
class Plaza_DepartamentoListSerializer(ModelSerializer):
    class Meta:
        model= unidad.Plaza_Departamento
        fields='__all__'

class Plaza_DepartamentoPutPostSerializer(ModelSerializer):
    class Meta:
        model= unidad.Plaza_Departamento
        fields=['estado','activo','plaza','departamento']