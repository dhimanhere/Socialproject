from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class MyAccountManager(BaseUserManager):
	def create_user(self, email, password = None):
		if not email :
			raise ValueError("Please enter a valid email")

		user = self.model(
				email = self.normalize_email(email),
			)
		user.set_password(password)
		user.save(using = self._db)
		return user

	def create_superuser(self, email, password):
		user = self.create_user(
				email = self.normalize_email(email),
				password = password,
			)

		user.is_admin = True
		user.is_staff = True
		user.is_active = True
		user.is_superuser = True
		user.save(using = self._db)
		return user

class MyUser(AbstractBaseUser):
	username = models.CharField(max_length = 90)
	name = models.CharField(max_length = 90)
	email = models.EmailField(max_length = 60, unique = True)
	facebook_page = models.CharField(max_length = 90, blank=True, null=True)
	twitter_username = models.CharField(max_length = 90, blank = True, null=True)
	date_joined = models.DateTimeField(verbose_name = 'date_joined', auto_now_add = True)
	last_login = models.DateTimeField(verbose_name = 'last_login', auto_now = True)
	is_admin = models.BooleanField(default = False)
	is_active = models.BooleanField(default = True)
	is_staff = models.BooleanField(default = False)
	is_superuser = models.BooleanField(default = False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = MyAccountManager()

	def has_perm(self, perm, obj = None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True