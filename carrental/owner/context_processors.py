from customer.models import Contact,Booking

def enquiries_context(request):
    enquiries = Contact.objects.filter(status="new").count()
    context = {"new_enquiries":enquiries}
    return context

def bookings_context(request):
    bookings = Booking.objects.filter(status="booked").count()
    context = {"new_bookings":bookings}
    return context