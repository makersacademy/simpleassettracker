from .models import CompanyUser
from .serializers import CompanyUserSerializer
from rest_framework import generics

class CompanyUserListCreate(generics.ListCreateAPIView):
    queryset = CompanyUser.objects.all()
    serializer_class = CompanyUserSerializer

class CompanyUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompanyUser.objects.all()
    serializer_class = CompanyUserSerializer