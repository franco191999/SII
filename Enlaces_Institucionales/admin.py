from django.contrib import admin
from Enlaces_Institucionales.models import *


class Enlace_admin(admin.ModelAdmin):
	pass
admin.site.register(Enlaces_Institucionales, Enlace_admin)

