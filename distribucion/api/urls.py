
from django.urls import path
from distribucion.api import views

urlpatterns=[

    path('Tipo_Movimiento_distribucion/',views.Tipo_MovimientoGAPIViewList.as_view()),
    path('Tipo_Movimiento_distribucion/<int:id>/',views.Tipo_MovimientoGAPIViewDetail.as_view()),

    path('Mesa_distribucion/',views.MesaGAPIViewList.as_view()),
    path('Mesa_distribucion/<int:id>/',views.MesaGAPIViewDetail.as_view()),

    path('Pedido_distribucion/',views.PedidoGAPIViewList.as_view()),
    path('Pedido_distribucion/<int:id>/',views.PedidoGAPIViewDetail.as_view()),

    path('Movimiento_distribucion/',views.MovimientoGAPIViewList.as_view()),
    path('Movimiento_distribucion/<int:id>/',views.MovimientoGAPIViewDetail.as_view()),

]