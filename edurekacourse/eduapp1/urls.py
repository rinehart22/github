from django.urls import path 
from .import views 

urlpatterns=[
    path('<int:couse_id>/', views.detail , name='details'),
    path('', views.course, name='course'),
]