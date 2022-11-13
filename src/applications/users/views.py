from django.contrib import auth
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import UserLoginForm
from .forms import UserProfileForm
from .forms import UserRegistrationForm
from .models import User


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("products:index"))
    else:
        form = UserLoginForm()
    context = {"form": form}
    return render(request, "users/login.html", context=context)


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Поздравляем! Вы успешно зарегистрировались!")
            return HttpResponseRedirect(reverse("users:login"))
    else:
        form = UserRegistrationForm()
    context = {"form": form}
    return render(request, "users/registration.html", context=context)


def profile(request):
    if request.method == "POST":
        form = UserProfileForm(
            instance=request.user, data=request.POST, files=request.FILES
        )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("users:profile"))
    else:
        form = UserProfileForm(instance=request.user)
    context = {"title": "Store - Профиль", "form": form}
    return render(request, "users/profile.html", context=context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("products:index"))
