from django.urls import path

from . import views

app_name = 'deeplearning'

urlpatterns = [
    path('', views.FileViewSet.as_view({'get': 'list'})),
    path('upload', views.FileViewSet.as_view({'post': 'create'})),
    path('train', views.TrainModelViewSet.as_view({'post': 'create'})),
    path('models', views.TrainModelViewSet.as_view({'get': 'retrieve'})),
]