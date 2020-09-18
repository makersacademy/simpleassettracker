from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from register.models import UnauthorizedUser
from companies.models import Company


class RegisterForm(forms.ModelForm):

  class Meta:
    model = UnauthorizedUser
    fields = ("Username", "Password", "Email")


class CompanyRegisterForm(forms.ModelForm):

  class Meta:
    model = Company
    fields = ("Name",)

  def __init__(self, *args, **kwargs):
    super(CompanyRegisterForm, self).__init__(*args, **kwargs)
    self.fields['Name'].label = "Company Name"
