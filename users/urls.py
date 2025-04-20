from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    ChangePasswordView,
    CustomTokenObtainPairView,
    LogoutView,
    UpdateUserActiveStatusView,
    UserCreateView,
    UserDeleteView,
    UserDetailView,
    UserListView,
    UserUpdateView,
)

urlpatterns = [
    path("", UserListView.as_view(), name="user-list"),
    path("register/", UserCreateView.as_view(), name="user-register"),
    path("login/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("change-password/", ChangePasswordView.as_view(), name="change-password"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("<int:id>/", UserDetailView.as_view(), name="user-detail"),
    path("<int:id>/update/", UserUpdateView.as_view(), name="user-update"),
    path("<int:id>/delete/", UserDeleteView.as_view(), name="user-delete"),
    path("<int:id>/set-active/", UpdateUserActiveStatusView.as_view(), name="user-set-active"),
]
