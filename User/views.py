from django.shortcuts import render,redirect
from .forms import SignUpForms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth import logout

                       

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForms(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
        else:
            # The form is not valid, handle the errors
            print(form.errors)  # Log the errors, or pass them to the template
    else:
        form = SignUpForms()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect("home1")
    else:
        form=AuthenticationForm()
        
    return render(request,"login.html" ,{'form':form})

def custom_logout(request):
    logout(request)
    return redirect('login')