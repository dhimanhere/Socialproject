from django.db import models
from account.models import MyUser

class Profile(models.Model):
	user = models.OneToOneField(MyUser, on_delete = models.CASCADE)
	username_twitter = models.CharField(max_length = 50)