
from django.urls import path
from carpeta.api import views

urlpatterns=[

    path('Categoria_carpeta/',views.CategoriaGAPIViewList.as_view()),
    path('Categoria_carpeta/<int:id>/',views.CategoriaGAPIViewDetail.as_view()),

    path('Ficheros_carpeta/',views.FicherosGAPIViewList.as_view()),
    path('Ficheros_carpeta/<int:id>/',views.FicherosGAPIViewDetail.as_view()),

    path('Objetivo_carpeta/',views.ObjetivoGAPIViewList.as_view()),
    path('Objetivo_carpeta/<int:id>/',views.ObjetivoGAPIViewDetail.as_view()),

    path('Tipo_Web_carpeta/',views.Tipo_WebGAPIViewList.as_view()),
    path('Tipo_Web_carpeta/<int:id>/',views.Tipo_WebGAPIViewDetail.as_view()),

    path('Ancho_Banda_carpeta/',views.Ancho_BandaGAPIViewList.as_view()),
    path('Ancho_Banda_carpeta/<int:id>/',views.Ancho_BandaGAPIViewDetail.as_view()),

    path('Anno_Unidad_carpeta/',views.Anno_UnidadGAPIViewList.as_view()),
    path('Anno_Unidad_carpeta/<int:id>/',views.Anno_UnidadGAPIViewDetail.as_view()),

    path('Resultados_carpeta/',views.ResultadosGAPIViewList.as_view()),
    path('Resultados_carpeta/<int:id>/',views.ResultadosGAPIViewDetail.as_view()),

    path('Conectividad_carpeta/',views.ConectividadGAPIViewList.as_view()),
    path('Conectividad_carpeta/<int:id>/',views.ConectividadGAPIViewDetail.as_view()),

    path('Pagina_Web_carpeta/',views.P_WebGAPIViewList.as_view()),
    path('Pagina_Web_carpeta/<int:id>/',views.P_WebGAPIViewDetail.as_view()),

    path('Enlaces_carpeta/',views.EnlacesGAPIViewList.as_view()),
    path('Enlaces_carpeta/<int:id>/',views.EnlacesGAPIViewDetail.as_view()),

    path('Aplicaciones_carpeta/',views.AplicacionesGAPIViewList.as_view()),
    path('Aplicaciones_carpeta/<int:id>/',views.AplicacionesGAPIViewDetail.as_view()),

    path('Documentos_carpeta/',views.DocumentosGAPIViewList.as_view()),
    path('Documentos_carpeta/<int:id>/',views.DocumentosGAPIViewDetail.as_view()),




]