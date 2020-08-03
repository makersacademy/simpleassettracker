from .models import Asset
from .serializers import AssetSerializer
from rest_framework import generics

class AssetListCreate(generics.ListCreateAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer