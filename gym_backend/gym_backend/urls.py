"""
URL configuration for gym_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users import views, admin_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/create/', views.create_user, name='create_user'),
    path('api/users/login/', views.login_user, name='login_user'),
    path('api/trainers/create/', views.create_trainer, name='create_trainer'),
    path('api/profile/create/', views.create_profile, name='create_profile'),
    path('api/profile/<int:user_id>/', views.get_profile, name='get_profile'),
    path('api/payment/update/', views.update_payment_status, name='update_payment_status'),
    
    # Admin APIs
    path('api/admin/users/all/', admin_views.get_all_users, name='get_all_users'),
    path('api/admin/users/paid/', admin_views.get_paid_users, name='get_paid_users'),
    path('api/admin/users/unpaid/', admin_views.get_unpaid_users, name='get_unpaid_users'),
    
    # Trainer management - specific paths before generic patterns
    path('api/admin/trainers/assign/', admin_views.assign_trainer_to_goal, name='assign_trainer_to_goal'),
    path('api/admin/trainers/remove/', admin_views.remove_trainer_from_goal, name='remove_trainer_from_goal'),
    path('api/admin/trainers/', admin_views.get_all_trainers, name='get_all_trainers'),
    path('api/admin/trainers/<str:goal>/', admin_views.get_trainers_by_goal, name='get_trainers_by_goal'),
]
