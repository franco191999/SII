
from django.urls import path
from transporte.api import views

urlpatterns=[

    path('Tipo_transporte/',views.TipoGAPIViewList.as_view()),
    path('Tipo_transporte/<int:id>/',views.TipoGAPIViewDetail.as_view()),

    path('Marca_transporte/',views.MarcaGAPIViewList.as_view()),
    path('Marca_transporte/<int:id>/',views.MarcaGAPIViewDetail.as_view()),

    path('Estado_Tec_transporte/',views.Estado_TecGAPIViewList.as_view()),
    path('Estado_Tec_transporte/<int:id>/',views.Estado_TecGAPIViewDetail.as_view()),

    path('Estado_Op_transporte/',views.Estado_OpGAPIViewList.as_view()),
    path('Estado_Op_transporte/<int:id>/',views.Estado_OpGAPIViewDetail.as_view()),

    path('Combustible_transporte/',views.CombustibleGAPIViewList.as_view()),
    path('Combustible_transporte/<int:id>/',views.CombustibleGAPIViewDetail.as_view()),

    path('Neumatico_transporte/',views.NeumaticoGAPIViewList.as_view()),
    path('Neumatico_transporte/<int:id>/',views.NeumaticoGAPIViewDetail.as_view()),

    path('Bateria_transporte/',views.BateriaGAPIViewList.as_view()),
    path('Bateria_transporte/<int:id>/',views.BateriaGAPIViewDetail.as_view()),

    path('Demanda_transporte/',views.DemandaGAPIViewList.as_view()),
    path('Demanda_transporte/<int:id>/',views.DemandaGAPIViewDetail.as_view()),

    path('Funcion_transporte/',views.FuncionGAPIViewList.as_view()),
    path('Funcion_transporte/<int:id>/',views.FuncionGAPIViewDetail.as_view()),

    path('Parque_transporte/',views.ParqueGAPIViewList.as_view()),
    path('Parque_transporte/<int:id>/',views.ParqueGAPIViewDetail.as_view()),

]