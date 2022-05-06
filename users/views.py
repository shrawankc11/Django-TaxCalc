from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created!')
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == "POST":
        form1 = UserUpdateForm(request.POST, instance=request.user)
        form2 = ProfileUpdateForm(request.POST,
                                  request.FILES,
                                  instance=request.user.profile)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            messages.success(request, f'Your account has been Updated!')
            return redirect("profile")
    else:
        form1 = UserUpdateForm(instance=request.user)
        form2 = ProfileUpdateForm(instance=request.user.profile)
    context = {
        "user_form": form1,
        "profile_form": form2,
    }
    return render(request, 'users/profile.html', context)
