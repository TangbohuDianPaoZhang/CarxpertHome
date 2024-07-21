from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('center/', views.center, name='center'),
    path('center_left/', views.center_left, name='center_left'),
    path('center_right2/', views.center_right2, name='center_right2'),
    path('centerRightChange/<int:energyType>', views.centerRightChange, name='centerRightChange'),
    path('bottomRight/', views.bottomRight, name='bottomRight')
]