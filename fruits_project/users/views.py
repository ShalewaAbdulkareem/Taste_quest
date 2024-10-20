from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        reg_form = UserRegistrationForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            messages.success(request, 'Registration Successfully')
            return redirect('users:login')
    else:
        reg_form = UserRegistrationForm()
    context = {
        'reg_form' : reg_form,
    }
    return render(request, 'user/register.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('users:dashboard')
        else:
            messages.error(request, 'Username or password Invalid')
    return render(request, 'user/login.html')