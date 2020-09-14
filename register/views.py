from django.shortcuts import render, redirect
from .forms import RegisterForm
from .forms import CompanyRegisterForm
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.
def register(response):
  if response.method == "POST":
    form = RegisterForm(response.POST)
    company_form = CompanyRegisterForm(response.POST)


    if form.is_valid and company_form.is_valid():
      user = form.save()
      company = company_form.save()
      company(Owned_by=User.models.get(username=user))
      company.save()
      messages.success(response, 'Your account and company has been created! Please sign in.')
      return redirect('login')

    else:
      form = RegisterForm()
      company_form = CompanyRegisterForm()
      messages.error(response, 'Invalid form submission')
      return render(response, "register/register.html", {"form": form, "company_form": company_form})

  else:
    company_form = CompanyRegisterForm()
    form = RegisterForm()
    return render(response, "register/register.html", {"form": form, "company_form": company_form})
