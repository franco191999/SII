from django.contrib import admin
from rrhh.models import *

# Register your models here.

class maquina_Admin(admin.ModelAdmin):
	pass
admin.site.register(maquina, maquina_Admin)

class registromaquina_Admin(admin.ModelAdmin):
	pass
admin.site.register(registromaquina, registromaquina_Admin)

class Nom_Cargo_Trabajador_Admin(admin.ModelAdmin):
	pass
admin.site.register(Nom_Cargo_Trabajador, Nom_Cargo_Trabajador_Admin)

class Nom_Titulo_Trabajador_Admin(admin.ModelAdmin):
	pass
admin.site.register(Nom_Titulo_Trabajador, Nom_Titulo_Trabajador_Admin)

class Nom_Habilidad_Trabajador_Admin(admin.ModelAdmin):
	pass
admin.site.register(Nom_Habilidad_Trabajador, Nom_Habilidad_Trabajador_Admin)


class Perfil_Admin_EnLinea(admin.TabularInline):
	model = Perfil
	extra=1
class Trabajador_Admin(admin.ModelAdmin):

	inlines=[Perfil_Admin_EnLinea]

	search_fields=['nombre']
	# list_display = ('nombre', 'perfil')
	list_filter=['municipio', 'cargo', 'perfil']
	list_per_page=10

admin.site.register(Trabajador, Trabajador_Admin)
