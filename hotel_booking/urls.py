from django.urls import path
from hotel_booking import views

urlpatterns = [
    path("rooms_list/", views.rooms_list, name="rooms_list"),
    path("book_room/", views.book_room, name="book_room"),
    path("booking_details/<int:pk>/", views.booking_details, name="booking_details"),

]