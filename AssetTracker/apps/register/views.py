from django.shortcuts import render, redirect
from .forms import RegisterForm
from .forms import CompanyRegisterForm
from .serializers import UnauthorizedUserSerializer
from .serializers import ApproveUserSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.contrib import messages
from ..register.models import UnauthorizedUser
from django.contrib.auth.models import User
from ..companyusers.models import CompanyUser
from ..companies.models import Company

# Create your views here.
def registercompany(response):
  if response.method == "POST":
    form = RegisterForm(response.POST)
    company_form = CompanyRegisterForm(response.POST)

    if form.is_valid() and company_form.is_valid():
      username = form.save()
      user_object = User.objects.get(username=username)
      company = company_form.save()
      company.owned_by=user_object
      company.save()
      company_user = CompanyUser.objects.create(user=user_object, company=company)
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
      company_name = response.POST["name"]
      user = form.save()
      user_object = User.objects.get(username=user)
      user_object.is_active = False
      company_object = Company.objects.get(name=company_name)
      unauth_user = UnauthorizedUser.objects.create(user=user_object, company=company_object)
      user_object.save()
      unauth_user.save()
      messages.success(response, 'Your account request has been submitted and is awaiting approval.')
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

class UnauthorizedUserList(generics.ListAPIView):
  serializer_class = UnauthorizedUserSerializer

  def get_queryset(self):
    queryset = UnauthorizedUser.objects.all()
    user = self.request.user
    try:
      company_id = CompanyUser.objects.get(user=user).company_id
    except CompanyUser.DoesNotExist:
      company_id = None

    if company_id is not None:
      queryset = queryset.filter(company=company_id).select_related('user')
      return queryset

    else:
      return Response(
        {"detail": "No company present"},
        status=status.HTTP_400_BAD_REQUEST
      )

class UnauthorizedUserDelete(generics.DestroyAPIView):
  queryset = UnauthorizedUser.objects.all()
  serializer_class = UnauthorizedUserSerializer

class ApproveUser(generics.RetrieveUpdateDestroyAPIView):
  queryset = User.objects.all()
  serializer_class = ApproveUserSerializer

  def update(self, request, *args, **kwargs):
    instance = self.get_object()
    instance.is_active = True
    instance.save()

    serializer = self.get_serializer(instance)

    return Response(serializer.data)
