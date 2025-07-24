from django.db import models
from django.contrib.auth.models import User
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Q

# Create your models here.

class Listing(models.Model):
    listing_id = models.UUIDField(default=uuid.uuid4(), editable=False, primary_key=True)
    host = models.ForeignKey(User, related_name="listings")
    name = models.CharField(max_length=250, null=False)
    description = models.TextField(max_length=250, null=False)
    address = models.CharField(max_length=200, null=False)
    pricepernight = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Review(models.Model):
    review_id = models.UUIDField(default=uuid.uuid4(), editable=False, primary_key=True)
    listing = models.ForeignKey(Listing, related_name="reviews", null=False)
    user = models.ForeignKey(User, related_name="reviews", null=False)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],
                                              null=False)
    
    class Meta:
        # This is to add the check Constraint on the rating
        constraints = [
            models.CheckConstraint(
                condition=Q(rating__gte=1, rating__lte=5),
                name = "rating__valid_number"
            )
        ]
    
    def __str__(self):
        return f"{self.review_id}"

class Booking(models.Model):
    STATUS = (
        ("Pending", "pending"),
        ("Confirmed", "confirmed"),
        ("Canceled", "canceled")
    )
    booking_id = models.UUIDField(default=uuid.uuid4(), editable=False, primary_key=True)
    listing = models.ForeignKey(Listing, related_name="bookings")
    user = models.ForeignKey(User, related_name="bookings")
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_price = models.DecimalField(max_digits=5, decimal_places=2)
    status =  models.CharField(max_length=9, choices=STATUS, default="pending")
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"User's{self.user__username} booking is: {self.status}"

