from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as auth_logout
from .models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.


@login_required
def index(request):
    if request.user.is_superuser:
        users = User.objects.all()
        context = {"users": users}
        return render(request, "accounts/index.html", context)
    else:
        return redirect("reviews:index")


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("reviews:index")
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get("next") or "reviews:index")
    else:
        form = AuthenticationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


def logout(request):
    auth_logout(request)
    return redirect("reviews:index")


@login_required
def detail(request, pk):
    if request.user.is_superuser:
        user_detail = User.objects.get(pk=pk)
        context = {
            "user_detail": user_detail,
        }
        return render(request, "accounts/detail.html", context)
    else:
        return redirect("reviews:index")


@login_required
def detail_update(request, pk):
    if request.user.is_superuser:
        user = User.objects.get(pk=pk)
        if request.method == "POST":
            form = CustomUserChangeForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return redirect("accounts:detail", user.pk)
        else:
            form = CustomUserChangeForm(instance=user)
        context = {
            "form": form,
        }
        return render(request, "accounts/detail_update.html", context)
    else:
        return redirect("reviews:index")


@login_required
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("accounts:profile")
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/update.html", context)


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("accounts:index")
    else:
        form = PasswordChangeForm(request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/change_password.html", context)


@login_required
def delete(request, pk):
    user = User.objects.get(pk=pk)
    user.delete()
    return redirect("reviews:index")


@login_required
def profile(request):
    profile = User.objects.get(pk=request.user.pk)
    context = {
        "profile": profile,
    }
    return render(request, "accounts/profile.html", context)
