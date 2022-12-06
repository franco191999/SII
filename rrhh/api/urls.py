

from django.urls import path
from rrhh.api import views

urlpatterns=[


    path('Habilidad_Trabajador_rrhh/',views.Habilidad_Trabajador_List),
    path('Habilidad_Trabajador_rrhh/<int:pk>/',views.Habilidad_Trabajador_detail),

    path('UserLog_rrhh/',views.UserLog_List),
    path('UserLog_rrhh/<int:pk>/',views.UserLog_detail),

    path('Maquina_rrhh/',views.Maquina_List),
    path('Maquina_rrhh/<int:pk>/',views.Maquina_detail),

    path('Registro_Maquina_rrhh/',views.Registro_Maquina_List),
    path('Registro_Maquina_rrhh/<int:pk>/',views.Registro_Maquina_detail),

    path('Trabajador_rrhh/',views.TrabajadorGAPIViewList.as_view()),
    path('Trabajador_rrhh/<int:id>/',views.TrabajadorGAPIViewDetail.as_view()),

    path('User_rrhh/',views.User_list),
    path('User_rrhh/<int:pk>/',views.User_detail),

    path('Perfil_rrhh/',views.Perfil_List),
    path('Perfil_rrhh/<int:pk>/',views.Perfil_detail),

    path('Cargo_Trabajador_rrhh/',views.Cargo_Trabajador_List),
    path('Cargo_Trabajador_rrhh/<int:pk>/',views.Cargo_Trabajador_detail),
    
    path('Titulo_Trabajador_rrhh/',views.Titulo_Trabajador_List),
    path('Titulo_Trabajador_rrhh/<int:pk>/',views.Titulo_Trabajador_detail),

    path('tokenlife/',views.token_life_List),
    path('tokenlife/<str:user>/',views.token_life_detail),

    path('login/',views.login),
    path('logout/',views.Logout.as_view()),

    path('change_password/',views.ChangePasswordView.as_view()),


]