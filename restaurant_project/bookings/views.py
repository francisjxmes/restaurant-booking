from django.shortcuts import render, redirect
from .forms import BookingForm

def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'bookings/success.html')
    else:
        form = BookingForm()
    return render(request, 'bookings/booking_form.html', {'form': form})
