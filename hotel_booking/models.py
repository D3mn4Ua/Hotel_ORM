from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    number = models.IntegerField()
    description = models.TextField()
    
    def __str__(self):
        return f"Room #{self.number}"
    
    class Meta:
        verbose_name = "Room"
        ordering = ["number"]

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="bookings")
    booked_at = models.DateTimeField(auto_now_add=True)
    booked_till = models.DateTimeField()

    def __str__(self):
        return f"User: {self.user.username} occupied room number - {self.room.number}"

    class Meta:
        verbose_name = "Booking"
        ordering = ["booked_at"]
