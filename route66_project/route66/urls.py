# importhing the files to put response on the paths

from django.urls import path
from . import views


# linking the paths to the response pages

urlpatterns = [
    path('', views.index, name='index'),
    path('gogetthegood/', views.gogetthegood(), name='good'),
    path('happyhappyjoyjoy/', views.happyhappyjoyjoy(), name='happy')
]