# Third party imports should be placed first
from rest_framework import generics
from .models import Asset
from .serializers import AssetSerializer

class AssetListCreate(generics.ListCreateAPIView):
	queryset = Asset.objects.all()
	serializer_class = AssetSerializer

	# def create(self, request, *args, **kwargs):
	# 	print(request)
	# 	print(args)
	# 	print(kwargs)
	# 	# extract data for mobileModel, validate and save
	# 	# get the id for the new entry and pass it to create
	# 	return super(AssetListCreate, self).create(request, *args, **kwargs) # grab return code, then if return code 200 - save, else undo what has just been done ie delete the save

class AssetDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Asset.objects.all()
	serializer_class = AssetSerializer
