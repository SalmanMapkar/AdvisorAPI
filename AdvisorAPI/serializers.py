from rest_framework import serializers
from .models import AdvisorDataModel, AdvisorBookingModel
from .validators import EmptyEmailorPassword
from django.core.exceptions import ValidationError


class AdvisorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model= AdvisorDataModel
        fields=['AdvisorName', 'AdvisorPhotoURL']


class AdvisorlistSerializer(serializers.ModelSerializer):
    class Meta:
        model=AdvisorDataModel
        fields=['AdvisorName', 'AdvisorPhotoURL', 'AdvisorId']


class AdvisorBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model= AdvisorBookingModel
        fields=['UserId', 'AdvisorId', 'BookingTime']

class AllBookedAdvisorSerializer(serializers.ModelSerializer):
    Advisor= AdvisorlistSerializer(many=True, read_only=True)
    class Meta:
        model=AdvisorBookingModel
        fields=["BookingTime", "BookingId", "AdvisorId", "Advisor"]
        depth=1



