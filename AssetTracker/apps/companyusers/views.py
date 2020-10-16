from .models import CompanyUser
from .serializers import CompanyUserSerializer
from rest_framework import generics

class CompanyUserListCreate(generics.ListCreateAPIView):
	queryset = CompanyUser.objects.all()
	serializer_class = CompanyUserSerializer

class CompanyUserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = CompanyUser.objects.all()
	serializer_class = CompanyUserSerializer

class CompanyUserList(generics.ListCreateAPIView):
	serializer_class = CompanyUserSerializer

	def get_queryset(self):
		queryset =  CompanyUser.objects.all()
		user = self.request.user
		company_id = CompanyUser.objects.get(user=user).company.id
		if company_id is not None:
			queryset = queryset.filter(company=company_id)
		return queryset
