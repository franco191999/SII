
from django.urls import path
from galeria.api import views

urlpatterns=[

    path('Categoria_galeria/',views.Categoria_Galeria_List),
    path('Categoria_galeria/<int:pk>/',views.Categoria_Galeria_detail),

    path('Imagenes_galeria/',views.GaleriaGAPIViewList.as_view()),
    path('Imagenes_galeria/<int:id>/',views.GaleriaGAPIViewDetail.as_view()),
]