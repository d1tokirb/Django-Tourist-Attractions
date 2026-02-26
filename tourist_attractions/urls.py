from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('details/<str:statename>/', views.details, name='details'),
]
