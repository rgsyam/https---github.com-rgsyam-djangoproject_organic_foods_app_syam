from django.urls import path
from OrganicFoodApp import views

urlpatterns = [
    
    #Header and Footer

    
    #Home1
    path("",views.home1,name="home1"),

    
    #Subscription
    path('subscription/',views.subscription,name='subscription'),
    
    # contact
    
    path("contact_views/",views.contact_views,name='contact'),
    
    # contact_success
    
    path('contact_success/',views.contact_success,name="contact_success"),
    
    path('aboutus/',views.aboutus,name='aboutus')
    

]

