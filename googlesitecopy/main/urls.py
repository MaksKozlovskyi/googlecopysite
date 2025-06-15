from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="google"),
    path('register/', views.register, name='register')
]
