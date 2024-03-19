from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('student/<int:pk>/add_achievement/', views.add_achievement, name='add_achievement'),
    path('profile/<str:username>/', views.student_profile, name='profile'),
    
    path('register/', views.user_register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
