from django.urls import path
from tienda_api import views

urlpatterns = [
    path('test/', views.HelloAppiView.as_view()),
]
