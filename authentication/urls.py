from django.template.defaulttags import url
from django.urls import path
from main import views
from authentication import views


urlpatterns = [
    path('login/', views.login_user, name='login_user'),
    path('register/', views.RegisterView.as_view(), name='register'),
    # path('login-user/', views.register, name='register'),
    path("logout/", views.logout_user, name='logout'),
]

# urlpatterns = [
#     path('login-register/', views.login_register, name='login_register'),
#     path("logout/", views.logout_user, name='logout'),
# ]