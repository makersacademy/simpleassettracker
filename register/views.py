from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import RegisterForm


# Create your views here.
def register(response):
  if response.method == "POST":
    form = RegisterForm(response.POST)
    if form.is_valid():
      form.save()
      messages.success(response, 'Your account has been created! Please sign in.')
      return redirect("/")

    else:
      form = RegisterForm()
      messages.error(response, 'Invalid form submission')
      return render(response, "register/register.html", {"form": form})

  else:
    form = RegisterForm()
    return render(response, "register/register.html", {"form": form})
