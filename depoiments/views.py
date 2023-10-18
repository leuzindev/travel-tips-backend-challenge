import random

from django.contrib.auth.models import User
from rest_framework import viewsets, generics

from .models import Depoiment
from .serializers import DepoimentsSerializers


class DepoimentsViewSet(viewsets.ModelViewSet):
    queryset = Depoiment.objects.all()
    serializer_class = DepoimentsSerializers


class RandomDepoimentsAPIView(generics.ListAPIView):
    serializer_class = DepoimentsSerializers

    def get_queryset(self):
        users = list(User.objects.all())
        random.shuffle(users)

        selected_users = users[:3]

        depoiments = []

        for user in selected_users:
            depoiment = Depoiment.objects.filter(user=user).first()
            if depoiment:
                depoiments.append(depoiment)

        return depoiments
