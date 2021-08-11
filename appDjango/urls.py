from django.urls import path #imports
from . import views

urlpatterns = [ #criando url
    path('', views.index,name='index')
]


