from django.urls import path,include
# from rest_framework.urlpatterns import format_suffix_patterns
from .views import EventList, EventDetail, DonationList,DonationDetail
from rest_framework.authtoken import views

urlpatterns = [
    path('api/v1/event/', EventList.as_view(),name="user-list"),
    path('api/v1/event/<int:pk>/', EventDetail.as_view()),
    path('api/v1/donate/', DonationList.as_view()),
    path('api/v1/donate/<int:pk>/', DonationDetail.as_view()),
    
]