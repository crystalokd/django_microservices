from django.db import models
from django.contrib.auth.models import User

 
class Pizzeria(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	address = models.CharField(max_length=512)
	phone = models.CharField(max_length=40)

class Pizza(models.Model):
	title = models.CharField(max_length=120)
	description = models.CharField(max_length=240)
	thumbnail_url = models.URLField(null=True)
	approved = models.BooleanField(default=False)
	creator = models.ForeignKey(Pizzeria, on_delete=models.CASCADE, null=True)

class Likes(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, null=True)