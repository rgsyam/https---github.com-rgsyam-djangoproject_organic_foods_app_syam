from django.urls import path
from User import views

urlpatterns = [
    path("signup/",views.signup,name='signup'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.custom_logout,name="logout"),
    
    
]
