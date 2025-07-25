from rest_framework import serializers
from .models import User, Review, Booking


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
    

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
