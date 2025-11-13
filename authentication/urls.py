from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    RegisterView,
    login_view,
    logout_view,
    current_user_view,
    ChangePasswordView,
    user_profile_view,
    update_profile_view,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('user/', current_user_view, name='current-user'),
    path('profile/', user_profile_view, name='user-profile'),
    path('profile/update/', update_profile_view, name='update-profile'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]
