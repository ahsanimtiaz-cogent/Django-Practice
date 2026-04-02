from django.urls import path
from .views import RegisterAPIView, UserListAPIView, UserDetailAPIView

urlpatterns = [
    path('users/', UserListAPIView.as_view()),              
    path('users/<int:pk>/', UserDetailAPIView.as_view()),  
    path('register/', RegisterAPIView.as_view()),          
]
