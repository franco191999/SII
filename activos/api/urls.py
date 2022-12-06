
from django.urls import path
from activos.api import views

urlpatterns=[

    path('Articulo_activos/',views.ArticuloGAPIViewList.as_view()),
    path('Articulo_activos/<int:id>/',views.ArticuloGAPIViewDetail.as_view()),

    path('Grupo_activos/',views.GrupoGAPIViewList.as_view()),
    path('Grupo_activos/<int:id>/',views.GrupoGAPIViewDetail.as_view()),

    path('Submayor_activos/',views.SubmayorGAPIViewList.as_view()),
    path('Submayor_activos/<int:id>/',views.SubmayorGAPIViewDetail.as_view()),

    path('Subgrupo_activos/',views.SubgrupoGAPIViewList.as_view()),
    path('Subgrupo_activos/<int:id>/',views.SubgrupoGAPIViewDetail.as_view()),

    path('Activo_activos/',views.ActivoGAPIViewList.as_view()),
    path('Activo_activos/<int:id>/',views.ActivoGAPIViewDetail.as_view()),

    path('Orden_Act_Fijo_activos/',views.Orden_Act_FijosGAPIViewList.as_view()),
    path('Orden_Act_Fijo_activos/<int:id>/',views.Orden_Act_FijosGAPIViewDetail.as_view()),

]