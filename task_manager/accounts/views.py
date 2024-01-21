from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from listings.models import Listing


def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Validation
        if password == password2:
            # Validate user name
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username taken')
                return redirect('register')
            else:
                # Validate user email
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email,
                                                    first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(request, 'Register success')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not mach')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return render(request, 'accounts/dashboard.html')
        else:
            messages.error(request, 'Invalid username/password')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            auth.logout(request)
        return redirect('index')

    return render(request, 'accounts/login.html')


def dashboard(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        listings = Listing.objects.filter(user=user).order_by('-list_date')
        return render(request, 'accounts/dashboard.html', {'listings': listings})

    return render(request, 'accounts/login.html')
