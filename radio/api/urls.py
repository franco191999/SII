
from django.urls import path
from radio.api import views

urlpatterns=[

    path('marca_radio/',views.Nombre_marcaGAPIViewList.as_view()),
    path('marca_radio/<int:id>/',views.Nombre_marcaGAPIViewDetail.as_view()),

    path('unidad_radio/',views.Unidad_radioGAPIViewList.as_view()),
    path('unidad_radio/<int:id>/',views.Unidad_radioGAPIViewDetail.as_view()),

    path('movil_radio/',views.MovilGAPIViewList.as_view()),
    path('movil_radio/<int:id>/',views.MovilGAPIViewDetail.as_view()),

    path('estaciones_fijas_radio/',views.Estaciones_fijasGAPIViewList.as_view()),
    path('estaciones_fijas_radio/<int:id>/',views.Estaciones_fijasGAPIViewDetail.as_view()),

    path('estaciones_moviles_radio/',views.Estaciones_movilesGAPIViewList.as_view()),
    path('estaciones_moviles_radio/<int:id>/',views.Estaciones_movilesGAPIViewDetail.as_view()),

    path('estaciones_portatiles_radio/',views.Estaciones_portatilesGAPIViewList.as_view()),
    path('estaciones_portatiles_radio/<int:id>/',views.Estaciones_portatilesGAPIViewDetail.as_view()),

    path('estaciones_repetidoras_radio/',views.Estaciones_repetidorasGAPIViewList.as_view()),
    path('estaciones_repetidoras_radio/<int:id>/',views.Estaciones_repetidorasGAPIViewDetail.as_view()),


    
]