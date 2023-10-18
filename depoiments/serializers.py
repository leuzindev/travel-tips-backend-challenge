from rest_framework import serializers

from .models import Depoiment


class DepoimentsSerializers(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Depoiment
        fields = ['photo', 'depoiment_text', 'user_name']
