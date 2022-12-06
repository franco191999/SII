

from django.urls import path
from Enlaces_Institucionales.api import views

urlpatterns=[


    path('Enlace_Enlaces_Institucionales/',views.Enlace_List),
    path('Enlace_Enlaces_Institucionales/<int:pk>/',views.Enlace_detail),
  
]