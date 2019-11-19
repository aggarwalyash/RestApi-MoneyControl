from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	phone = models.CharField(max_length=10)
	dob = models.DateField()

	def __str__(self):
		return self.user.username

class Wallet(models.Model):
	user = models.ForeignKey(User,related_name='wallets',on_delete=models.CASCADE)
	wallet_name = models.CharField(max_length=100)
	wallet_description = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	is_shared = models.BooleanField(default=False)

	def __str__(self):
		return self.wallet_name + " --> " + self.user.username

class Operation(models.Model):
	STATUS_CHOICES = (
	    ('1', "Added"),
	    ('2', "Spent"),
	)
	wallet = models.ForeignKey(Wallet,related_name='operations',on_delete=models.CASCADE)
	action = models.CharField(choices=STATUS_CHOICES,max_length=1)
	amount = models.DecimalField(max_digits=10,decimal_places=2)
	note = models.CharField(max_length=255,null=True,blank=True)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.wallet.wallet_name + " --> " + self.wallet.user.username


class ContactBook(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	phone = models.CharField(max_length=10)
	email = models.EmailField(null=True,blank=True)

	def __str__(self):
		return self.user.username + " -->  " + self.name + ", " + self.phone + ", " + self.email

class LendingBook(models.Model):
	STATUS_CHOICES = (
            ('1', "Lend"),
            ('2', "Received"),)
	user = models.ForeignKey(User,related_name='lendingbooks',on_delete=models.CASCADE)
	contact = models.ForeignKey(ContactBook,on_delete=models.SET_NULL,null=True)
	action = models.CharField(choices=STATUS_CHOICES,max_length=1)
	amount = models.DecimalField(max_digits=10,decimal_places=2)
	note = models.CharField(max_length=255,null=True,blank=True)
	when = models.DateTimeField(auto_now_add=True)
	returned = models.DateTimeField(blank=True,null=True)
