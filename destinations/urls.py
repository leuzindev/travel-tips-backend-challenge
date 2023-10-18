from django.urls import path

from .views import DestinationsViewSet

urlpatterns = [
    path('destinations', DestinationsViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('destinations/<int:pk>',
         DestinationsViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
