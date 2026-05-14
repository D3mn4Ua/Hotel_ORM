from django.shortcuts import render, redirect
from .models import  Room, Booking
from django.http import HttpResponse

def rooms_list(request):
    rooms = Room.objects.all()
    context = {
        "rooms": rooms,
    }
    return render(
        request,
        "booking/rooms_list.html",
        context=context
    )

def book_room(request):
    if request.method == "POST":
        room_number = request.POST.get("room_number")
        booked_till = request.POST.get("booked_till")

        try:
            room = Rool.objects.get(number=room_number)
        except ValueError:
            return HttpResponse(
                "Wrong value for an integer field.",
                status=400
            )
        except Room.DoesNotExist:
            return HttpResponse(
                "Room number does not exist",
                status=404
            )
        booking = Booking.objects.create(
            user=request.user,
            room=room,
            booked_till=booked_till
        )
        return redirect("booking_details", pk)
    else:
        return render(
            request,
            "booking/booking_form.html"
        )

def booking_details(request, pk):
    try:
        booking = Booking.objects.get(id=pk)
        context = {
            "booking": booking
        }
        return render(
            request,
            "booking/booking_details.html",
            context=context
        )
    except:
        return HttpResponse(
            "Room number does not exist",
            status=404
        )