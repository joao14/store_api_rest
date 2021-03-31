from django.urls import path
from tienda_api import views

urlpatterns = [
    path('test/', views.HelloAppiView.as_view()),
    path('client/', views.ClientAppiView.as_view()),
    path('product/', views.ProductAppiView.as_view()),
    path('store/', views.StoreAppiView.as_view()),
    path('album/', views.AlbumApiView.as_view()),
    path('track/', views.TrackApiView.as_view()),
]
