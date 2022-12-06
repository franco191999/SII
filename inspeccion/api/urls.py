
from django.urls import path
from inspeccion.api import views

urlpatterns=[

    path('Estado_Deficiencia_inspeccion/',views.Estado_DeficienciaGAPIViewList.as_view()),
    path('Estado_Deficiencia_inspeccion/<int:id>/',views.Estado_DeficienciaGAPIViewDetail.as_view()),

    path('Aspecto_Deficiencia_inspeccion/',views.Aspecto_DeficienciaGAPIViewList.as_view()),
    path('Aspecto_Deficiencia_inspeccion/<int:id>/',views.Aspecto_DeficienciaGAPIViewDetail.as_view()),

    path('Tipo_Visita_inspeccion/',views.Tipo_VisitaGAPIViewList.as_view()),
    path('Tipo_Visita_inspeccion/<int:id>/',views.Tipo_VisitaGAPIViewDetail.as_view()),

    path('Visita_inspeccion/',views.VisitaGAPIViewList.as_view()),
    path('Visita_inspeccion/<int:id>/',views.VisitaGAPIViewDetail.as_view()),

    path('Deficiencia_inspeccion/',views.DeficienciaGAPIViewList.as_view()),
    path('Deficiencia_inspeccion/<int:id>/',views.DeficienciaGAPIViewDetail.as_view()),

    path('Deficiencia_Tarea_inspeccion/',views.DeficienciaXtareaGAPIViewList.as_view()),
    path('Deficiencia_Tarea_inspeccion/<int:id>/',views.DeficienciaXtareaGAPIViewDetail.as_view()),

   
]