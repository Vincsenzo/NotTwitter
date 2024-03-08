from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register-user/', views.register_user, name='register_user'),
]
