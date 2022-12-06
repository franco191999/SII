from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
	
    path('api/', include('finanzas.api.urls')),
    path('api/', include('rrhh.api.urls')),
    path('api/', include('mensajes.api.urls')),
    path('api/', include('unidad.api.urls')),
    path('api/', include('galeria.api.urls')),
    path('api/', include('carpeta.api.urls')),
    path('api/', include('inspeccion.api.urls')),
    path('api/', include('presupuesto.api.urls')),
    path('api/', include('transporte.api.urls')),
    path('api/', include('activos.api.urls')),
    path('api/', include('distribucion.api.urls')),
    path('api/', include('telefonos.api.urls')),
    path('api/', include('tareas.api.urls')),
    path('api/', include('Enlaces_Institucionales.api.urls')),
    path('api/', include('radio.api.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)