from . import views
from django.urls import path

urlpatterns = [
    path('', views.archives, name='archives'),
    path('<str:arc>', views.gallerys, name='gallerys'),
    path('gallery/<str:gal>/', views.galleryimages, name='galleryimages'),
]