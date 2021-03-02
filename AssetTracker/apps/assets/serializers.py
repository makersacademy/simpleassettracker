from rest_framework import serializers
from .models import Asset, MobileCustomData

class MobileSerializer(serializers.ModelSerializer):

	class Meta:
		model = MobileCustomData
		fields = '__all__'

class AssetSerializer(serializers.ModelSerializer):
	# imei = serializers.CharField()

	class Meta:
		model = Asset
		fields = '__all__'

	def validate_imei(self, *args, **kwargs)

	def create(self, validated_data):
		validated_data['imei'] = 'test value in create method'
		print(validated_data)
		imei = validated_data.pop('imei')
		try:
			validated_data['mobile_custom_data'] = MobileCustomData.objects.create(imei=imei)
		except Exception as e:
			print('To do, handle this error')
			raise e
		return super(AssetSerializer, self).create(validated_data)
