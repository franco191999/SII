
from django.urls import path
from presupuesto.api import views

urlpatterns=[

    path('Presupuesto_Unidad_presupuesto/',views.Presupuesto_UnidadGAPIViewList.as_view()),
    path('Presupuesto_Unidad_presupuesto/<int:id>/',views.Presupuesto_UnidadGAPIViewDetail.as_view()),

    path('Orden_Servicio_Unidad_presupuesto/',views.Orden_Servicio_UnidadGAPIViewList.as_view()),
    path('Orden_Servicio_Unidad_presupuesto/<int:id>/',views.Orden_Servicio_UnidadGAPIViewDetail.as_view()),

    
]