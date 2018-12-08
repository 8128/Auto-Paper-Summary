from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('info/', views.user_info, name='user_info'),
    path('history/', views.history, name='user_history'),
]
