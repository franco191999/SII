
from django.urls import path
from telefonos.api import views

urlpatterns=[

    path('Pizarra_telefonos/',views.PizarraGAPIViewList.as_view()),
    path('Pizarra_telefonos/<int:id>/',views.PizarraGAPIViewDetail.as_view()),

    path('Telefono_Fijo_telefonos/',views.Telefono_FijoGAPIViewList.as_view()),
    path('Telefono_Fijo_telefonos/<int:id>/',views.Telefono_FijoGAPIViewDetail.as_view()),

    path('Extencion_telefonos/',views.ExtencionGAPIViewList.as_view()),
    path('Extencion_telefonos/<int:id>/',views.ExtencionGAPIViewDetail.as_view()),


]