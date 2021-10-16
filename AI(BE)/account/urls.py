from django.urls import path    
from rest_framework_jwt.views import verify_jwt_token
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login', views.Login.as_view({'post': 'create'})),
]