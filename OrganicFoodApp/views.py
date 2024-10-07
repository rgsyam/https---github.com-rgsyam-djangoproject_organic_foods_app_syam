from django.shortcuts import render,redirect
from .models import Special_Offers,Subscription,Contact
from .forms import SubscriptionsForm,ContactForm


# Create your views here.

def home1(request):
   
    all_offer_items=Special_Offers.objects.filter(category="all offers")
    fruits_items=Special_Offers.objects.filter(category="fruits")
    vegatables_items=Special_Offers.objects.filter(category="vegatables")
    Offers={
        'all_offer_items':all_offer_items,
        'fruits_items':fruits_items,
        'vegatables_items':vegatables_items,
    }
    
    
    return render(request,"home1.html",Offers)






def subscription(request):
    if request.method == 'POST':
        form = SubscriptionsForm(request.POST)
        if form.is_valid():
            Subscription.objects.create(
                email=form.cleaned_data['email'],
            )
            return redirect('/ ')
        else:
             form = SubscriptionsForm()
    return render(request,"subscription.html" ,{'form':form})

def contact_views(request):
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            Contact.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message'],
                
            )
            return redirect("contact_success")
        else:
            form=ContactForm()
    return render (request,"contact.html")

def contact_success(request):
    return render (request,"contact_success.html")

def aboutus(request):
    return render (request,"aboutus.html")