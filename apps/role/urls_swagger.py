# urls.py
from django.urls import path
from .api.views import RoleListCreateView, CustomUserListCreateView

urlpatterns = [
    path('roles/', RoleListCreateView.as_view(), name='role-list-create'),
    path('users/', CustomUserListCreateView.as_view(), name='user-list-create'),
]
