

from django.urls import path
from tareas.api import views

urlpatterns=[


    path('Categoria_tareas/',views.Categoria_Tarea_List),
    path('Categoria_tareas/<int:pk>/',views.Categoria_Tarea_detail),

    path('Clasificacion_tareas/',views.Clasificacion_Tareas_List),
    path('Clasificacion_tareas/<int:pk>/',views.Clasificacion_Tareas_detail),

    path('Prioridad_tareas/',views.Prioridad_Tareas_List),
    path('Prioridad_tareas/<int:pk>/',views.Prioridad_Tareas_detail),

    path('Estado_tareas/',views.Estado_Tareas_List),
    path('Estado_tareas/<int:pk>/',views.Estado_Tareas_detail),

    path('Frecuencia_tareas/',views.Frecuencia_Tareas_List),
    path('Frecuencia_tareas/<int:pk>/',views.Frecuencia_Tareas_detail),

    path('Tarea_tareas/',views.Tareas_list),
    path('Tarea_tareas/<int:pk>/',views.Tareas_detail),
   
]