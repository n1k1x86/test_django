from rest_framework import serializers
from .models import AdvModel

class AdvModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvModel
        fields = '__all__'