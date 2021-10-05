from django.urls import path    

from . import views

app_name = 'files'

urlpatterns = [
    path('', views.FilesViewSet.as_view({'get': 'list'})),
    path('upload', views.FilesViewSet.as_view({'post': 'create'})),
]