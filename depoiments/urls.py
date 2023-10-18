from django.urls import path

from .views import DepoimentsViewSet, RandomDepoimentsAPIView

urlpatterns = [
    path('depoiments', DepoimentsViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('depoiments/<int:pk>', DepoimentsViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('depoiments-home', RandomDepoimentsAPIView.as_view()),
]
