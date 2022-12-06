from django.urls import path
from unidad.api import views

urlpatterns=[

    path('Tipo_Plaza_unidad/',views.Tipo_Plaza_List),
    path('Tipo_Plaza_unidad/<int:pk>/',views.Tipo_Plaza_detail),

    path('Nombre_Plaza_unidad/',views.Nombre_Plaza_List),
    path('Nombre_Plaza_unidad/<int:pk>/',views.Nombre_Plaza_detail),

    path('Tipo_Unidad_Org_unidad/',views.Tipo_Unidad_Org_List),
    path('Tipo_Unidad_Org_unidad/<int:pk>/',views.Tipo_Unidad_Org_detail),

    path('Unidad_Org_unidad/',views.Unidad_Org_List),
    path('Unidad_Org_unidad/<int:pk>/',views.Unidad_Org_detail),

    path('Provincia_unidad/',views.Provincia_List),
    path('Provincia_unidad/<int:pk>/',views.Provincia_detail),

    path('Municipio_unidad/',views.Municipio_List),
    path('Municipio_unidad/<int:pk>/',views.Municipio_detail),

    path('Tipo_Unidad_unidad/',views.Tipo_Unidad_List),
    path('Tipo_Unidad_unidad/<int:pk>/',views.Tipo_Unidad_detail),

    path('Perfil_Unidad_unidad/',views.Perfil_Unidad_List),
    path('Perfil_Unidad_unidad/<int:pk>/',views.Perfil_Unidad_detail),

    path('Nivel_Unidad_unidad/',views.Nivel_Unidad_List),
    path('Nivel_Unidad_unidad/<int:pk>/',views.Nivel_Unidad_detail),

    path('Unidad_unidad/',views.UnidadGAPIViewList.as_view()),
    path('Unidad_unidad/<int:id>/',views.UnidadGAPIViewDetail.as_view()),

    path('Departamento_unidad/',views.Departamento_List),
    path('Departamento_unidad/<int:pk>/',views.Departamento_detail),

    path('Plaza_Departamento_unidad/',views.Plaza_Departamento_List),
    path('Plaza_Departamento_unidad/<int:pk>/',views.Plaza_Departamento_detail),
    ]