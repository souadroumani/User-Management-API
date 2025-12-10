from django.urls import path
from .views import RegisterView , LoginView , UsersListView , UserDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/', UsersListView.as_view(), name='users-list'),
   path('users/<int:user_id>/', UserDetailView.as_view(), name='user-detail'),


]
