from django.urls import path
from .views import CustomUserListCreateAPIView, CustomUserRetrieveUpdateAPIView,\
    ProfileListCreateAPIView, ProfileRetrieveUpdateAPIView, GetRoutes,CustomUserLoginAPIView
from rest_framework.authtoken import views

urlpatterns = [
    path('', GetRoutes.as_view(), name='get-route'),
    path('api/v1/users/', CustomUserListCreateAPIView.as_view(), name='user-list-create'),
    path('api/v1/login/', CustomUserLoginAPIView.as_view(), name='login'),
    path('api/v1/users/<int:pk>/', CustomUserRetrieveUpdateAPIView.as_view(), name='user-detail'),
    path('api/v1/profiles/', ProfileListCreateAPIView.as_view(), name='profile-list-create'),
    path('api/v1/profiles/<int:pk>/', ProfileRetrieveUpdateAPIView.as_view(), name='profile-detail'),
    path('api-token-auth/', views.obtain_auth_token),
]
