from django.shortcuts import render, redirect
from .forms import SignupForm
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth.hashers import make_password

def index(request):
    user_name = request.session.get('username', None)
    users = CustomUser.objects.all() 
    return render(request, 'index.html', {'user_name': user_name,'users': users})

def signup(request):
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']

                # Hash the password before saving
                hashed_password = make_password(password)

                # Create the new user
                user = CustomUser(username=username, email=email, password=hashed_password)
                user.save()

                request.session['username'] = user.username

                # Add success message
                messages.success(request, f'Welcome {username}, you have successfully signed up!')

                # Redirect to index page
                return redirect('index')
            else:
                print(form.errors)
                messages.error(request, 'Please fix the errors below.')

        else:
            form = SignupForm()

        return render(request, 'signup.html', {'form': form})




