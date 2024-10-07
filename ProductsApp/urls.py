from django.urls import path
from ProductsApp import views

urlpatterns = [
    path("products/",views.products,name="product"),
    path('booking/<int:product_id>/',views.booking,name="booking"),
    path ("show/",views.show_order,name='view_order'),
    path("booking_success/",views.booking_success,name="booking_success"),
    
    
]
