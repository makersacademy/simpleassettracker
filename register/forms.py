from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from companies.models import Company


class RegisterForm(UserCreationForm):
  email = forms.EmailField()

  class Meta:
    model = User
    fields = ("username", "email", "password1", "password2")


class CompanyRegisterForm(forms.ModelForm):

  class Meta:
    model = Company
    fields = ("Name",)

  def __init__(self, *args, **kwargs):
    super(CompanyRegisterForm, self).__init__(*args, **kwargs)
    self.fields['Name'].label = "Company Name"


