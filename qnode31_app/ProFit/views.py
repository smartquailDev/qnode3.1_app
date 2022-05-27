from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, \
                   UserEditForm, ProfileEditForm, UserRequestForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from .models import Profile, UserRequest

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            remember_me = form.cleaned_data['remember_me']
            cd = form.cleaned_data
            user = authenticate(request,
                                Usuario= cd['username'],
                                Contraseña= cd['password'],
                                remember_me = cd['remember_me'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if not remember_me:
                        request.session.set_expiry(0)

                    return HttpResponse('Authenticated '\
                                        'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return render(request, 'ProFit/dashboard.html')
    else:
        form = LoginForm()
    return render(request, 'ProFit/login.html', {'form': form})



@login_required
def dashboard(request):
    return render(request,'ProFit/dashboard.html',{'section':'dashboard'})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            Profile.objects.create(user=new_user)
            return render(request,
                          'ProFit/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'ProFit/register.html',
                  {'user_form': user_form})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,
                  'ProFit/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})


def user_request(request):
    if request.method == 'POST':
        user_request_form = UserRequestForm(request.POST)
        if user_request_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_profit = user_request_form.save(commit=False)
            # Set the chosen password
           
            # Save the User object
            new_profit.save()
            # Create the user profile
            UserRequest.objects.create(admin_user=new_profit)
            return render(request,
                          'ProFit/request_done.html',
                          {'new_profit': new_profit})
    else:
        user_request_form = UserRequestForm()
    return render(request,
                  'ProFit/request.html',
                  {'user_request_form': user_request_form })


