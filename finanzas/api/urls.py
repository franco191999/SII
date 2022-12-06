
from django.urls import path
from finanzas.api import views

urlpatterns=[

    path('Partida_finanzas/',views.PartidaGAPIViewList.as_view()),
    path('Partida_finanzas/<int:id>/',views.PartidaGAPIViewDetail.as_view()),

    path('Presupuesto_finanzas/',views.PresupuestoGAPIViewList.as_view()),
    path('Presupuesto_finanzas/<int:id>/',views.PresupuestoGAPIViewDetail.as_view()),

    path('Retiro_finanzas/',views.RetiroGAPIViewList.as_view()),
    path('Retiro_finanzas/<int:id>/',views.RetiroGAPIViewDetail.as_view()),

   
]