from django.urls import path

from . import views

app_name = 'deeplearning'

urlpatterns = [
    path('', views.FileViewSet.as_view({'get': 'list'})),
    path('upload', views.FileViewSet.as_view({'post': 'create'})),
    path('train', views.TrainViewSet.as_view({'post': 'retrieve'})),
    path('models', views.TrainModelViewSet.as_view({'get': 'retrieve'})),
    path('log', views.LogView.as_view()),
    path('log/api', views.LogModelViewt.as_view({'post': 'create'})),
]