from rest_framework import generics

from .models import Asset
from .serializers import AssetSerializer


class AssetListCreate(generics.ListCreateAPIView):
  queryset = Asset.objects.all()
  serializer_class = AssetSerializer


class AssetDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Asset.objects.all()
  serializer_class = AssetSerializer
