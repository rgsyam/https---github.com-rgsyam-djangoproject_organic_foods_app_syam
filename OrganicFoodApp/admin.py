from django.contrib import admin
from .models import Special_Offers
from . models import Subscription
from . models import Contact


# Register your models here.

#Special_Offers
admin.site.register(Special_Offers)

#Subscription
admin.site.register(Subscription)

# contact
admin.site.register(Contact)



