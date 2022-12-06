

from django.urls import path
from mensajes.api import views

urlpatterns=[


    path('Categoria_mensajes/',views.Categoria_Mensaje_List),
    path('Categoria_mensajes/<int:pk>/',views.Categoria_Mensaje_detail),

    path('Mensaje_mensajes/',views.Mensaje_List),
    path('Mensaje_mensajes/<int:pk>/',views.Mensaje_detail),

    path('Eliminar_Destinatario_mensajes/',views.Eliminar_Destinatario_List),
    path('Eliminar_Destinatario_mensajes/<int:pk>/',views.Eliminar_Destinatario_detail),

    path('Mensaje_Leido_mensajes/',views.Mensaje_Leido_List),
    path('Mensaje_Leido_mensajes/<int:pk>/',views.Mensaje_Leido_detail),


   
]