from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('summary/', views.summary, name='summary'),
    path('about/', views.about, name='about'),
    path('info/', views.user_info, name='user_info'),
    path('history/', views.history, name='user_history'),
    # path('shortinput/', views.short_input, name='short_input')
]
