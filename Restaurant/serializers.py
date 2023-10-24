from rest_framework import serializers
from .models import Menu,Booking

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['booking_id', 'Title', 'price', 'inventory']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'