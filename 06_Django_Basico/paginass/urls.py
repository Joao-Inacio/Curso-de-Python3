from django.urls import path
from . import views

# /blog/
urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
]
