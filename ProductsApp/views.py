
from django.shortcuts import render,redirect,get_object_or_404
from .models import Products,Booking
from django.contrib.auth.decorators import login_required
from . import forms,models


# Create your views here.
def products(request):
    fruits_items=Products. objects.filter(category="fruits")
    vegetables_items=Products. objects.filter(category="vegetables")
    non_veg=Products. objects.filter(category="non-veg")
    context={
        'fruits_items':fruits_items,
        'vegetables_items':vegetables_items,
        'non_veg': non_veg,
        
    }
    return render(request,"products.html", context)


def booking(request,product_id):
    product = get_object_or_404(Products, id=product_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')

        Booking.objects.create(
            customer=request.user,
            product=product,
            quantity=quantity,
            address=address,
            mobile=mobile,
        )
        return redirect('booking_success')  # Make sure this name matches your URL pattern
    return render(request, 'Booking.html', {'product': product})

def show_order(request):
    bookings = Booking.objects.filter(customer=request.user)
    return render (request,"show_order.html", {'bookings': bookings})

def booking_success(request):
    return render (request,'booking_succes.html')