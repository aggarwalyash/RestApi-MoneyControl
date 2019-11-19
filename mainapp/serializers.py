from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
	#wallets = serializers.RelatedField(many=True,queryset=Wallet.objects.all())
	wallets = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	#profile = serializers.RelatedField(read_only=True)
	phone = serializers.ReadOnlyField(source='profile.phone')
	dob = serializers.ReadOnlyField(source='profile.dob')
	class Meta:
		model = User
		fields = ['id','username','email','phone','dob','wallets']


class WalletSerializer(serializers.ModelSerializer):
	operations = serializers.PrimaryKeyRelatedField(many=True,queryset=Operation.objects.all())
	class Meta:
		model = Wallet
		fields = ['id','user','wallet_name','wallet_description','created','is_shared','operations']


class ContactBookSerializer(serializers.ModelSerializer):

	# user = serializers.ReadOnlyField(source='user.username')
	class Meta:
		model = ContactBook
		fields = '__all__'
		# fields = ['id','name','phone','email','user']


class LendingBookSerializer(serializers.ModelSerializer):
	# contact = serializers.RelatedField(read_only=True)
	#
	class Meta:
		model = LendingBook
		fields = ['id','user','contact','action','amount','note','when','returned']
