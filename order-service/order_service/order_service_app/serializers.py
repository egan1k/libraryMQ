from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Orders


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'
