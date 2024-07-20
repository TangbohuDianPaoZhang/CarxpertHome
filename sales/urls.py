from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('center/', views.center, name='center'),
    path('center_left/', views.center_left, name='center_left'),
]