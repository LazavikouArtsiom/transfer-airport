from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Booking, Direction

def indexView(request):
    template_name = 'booking/base.html'
    booking_form = BookingForm()
    if request.method == 'POST':
        booking_form = BookingForm(request.POST or None)
        if booking_form.is_valid():
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            city = request.POST.get('city')
            airport = request.POST.get('airport')
            count = request.POST.get('count')
            order_date = request.POST.get('order_date')
            if request.POST.get('is_back') == 'on':
                is_back = True
            else:
                is_back = False
            back_date = request.POST.get('back_date')
            notes = request.POST.get('notes')

            booking = Booking.objects.create(name=name, email=email ,city=city, phone=phone,
                                            airport=airport, count=count, order_date=order_date,
                                            is_back=is_back, back_date=back_date, notes=notes)
            booking.save()
            return redirect('/')

    context = {
        'booking_form': booking_form,
        'directions': Direction.objects.order_by('city','airport'),
    }
    return render(request, template_name, context)