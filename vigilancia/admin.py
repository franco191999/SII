from django.contrib import admin
from vigilancia.models import *

class universotratamientofocal_admin(admin.ModelAdmin):
	pass
admin.site.register(universotratamientofocal, universotratamientofocal_admin)

class universotratamientoadulticida_admin(admin.ModelAdmin):
	pass
admin.site.register(universotratamientoadulticida, universotratamientoadulticida_admin)

class tratamientofocal_admin(admin.ModelAdmin):
	pass
admin.site.register(tratamientofocal, tratamientofocal_admin)

class tratamientoadulticida_admin(admin.ModelAdmin):
	pass
admin.site.register(tratamientoadulticida, tratamientoadulticida_admin)

class recursos_admin(admin.ModelAdmin):
	pass
admin.site.register(recursos, recursos_admin)

class centrospositivos_admin(admin.ModelAdmin):
	pass
admin.site.register(centrospositivos, centrospositivos_admin)

class centroscerrados_admin(admin.ModelAdmin):
	pass
admin.site.register(centroscerrados, centroscerrados_admin)

class albopictus_admin(admin.ModelAdmin):
	pass
admin.site.register(albopictus, albopictus_admin)

class centrospriorizados_admin(admin.ModelAdmin):
	pass
admin.site.register(centrospriorizados, centrospriorizados_admin)

