from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('summary/', views.summary, name='summary'),
    path('about/', views.about, name='about'),
    path('info/', views.user_info, name='user_info'),
    path('history/', views.history, name='user_history'),
    path('eg1/', views.eg1, name='example1'),
    path('eg2/', views.eg2, name='example2'),
    path('eg3/', views.eg3, name='example3'),
    path('eg4/', views.eg4, name='example4')
]
