from django.shortcuts import render, redirect
from .forms import RegisterForm
from .forms import CompanyRegisterForm
from django.contrib import messages
from django.contrib.auth.models import User
from companyusers.models import CompanyUser
from companies.models import Company

# Create your views here.
def registercompany(response):
  if response.method == "POST":
    form = RegisterForm(response.POST)
    company_form = CompanyRegisterForm(response.POST)

    if form.is_valid() and company_form.is_valid():
      username = form.save()
      user_object = User.objects.get(username=username)
      company = company_form.save()
      company.Owned_by=user_object
      company.save()
      company_user = CompanyUser.objects.create(User=user_object, Company=company)
      messages.success(response, 'Your account and company has been created! Please sign in.')
      return redirect('login')

    else:
      form = RegisterForm()
      company_form = CompanyRegisterForm()
      messages.error(response, 'Invalid form submission')
      return render(response, "register/registercompany.html", {"form": form, "company_form": company_form})

  else:
    company_form = CompanyRegisterForm()
    form = RegisterForm()
    return render(response, "register/registercompany.html", {"form": form, "company_form": company_form})

def registeruser(response):
  if response.method == "POST":
    form = RegisterForm(response.POST)
    company_form = CompanyRegisterForm(response.POST)

    if form.is_valid():
      company_name = response.POST["Name"]
      username = form.save()
      user_object = User.objects.get(username=username)
      company_object = Company.objects.get(Name=company_name)
      CompanyUser.objects.create(User=user_object, Company=company_object)
      messages.success(response, 'Your account has been created! Please sign in.')
      return redirect('login')

    else:
      form = RegisterForm()
      company_form = CompanyRegisterForm()
      messages.error(response, 'Invalid form submission')
      return render(response, "register/registeruser.html", {"form": form, "company_form": company_form})

  else:
    company_form = CompanyRegisterForm()
    form = RegisterForm()
    return render(response, "register/registeruser.html", {"form": form, "company_form": company_form})

def preregisterview(response):
  return render(response, "register/preregister.html", {})
