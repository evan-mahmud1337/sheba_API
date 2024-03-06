from django.urls import path, include
from . import views

urlpatterns = [
    path('api/v2/galleries/', views.GalleryList.as_view()),
   
]

