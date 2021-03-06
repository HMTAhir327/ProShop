from django.urls import path
from base.views import user_views as views

urlpatterns = [
    # path('users/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', views.registerUser, name="register"),


    path('profile', views.getUserProfile, name="users-profile"),
    path('', views.getUsers, name="users"),
]