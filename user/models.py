from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.db import models
import uuid

class UserManager(BaseUserManager):
	def create_user(self, email, username, password, **extra_fields):
		if not email:
			raise ValueError(('You must provide an email address.'))
		
		email = self.normalize_email(email)
		user = self.model(email=email, username=username, **extra_fields)
		user.set_password(password)
		user.save()

		return user
	
	def create_superuser(self, email, username, password, **extra_fields):
		
		extra_fields.setdefault("is_staff", True)
		extra_fields.setdefault("is_superuser", True)

		if extra_fields.get("is_staff") is not True:
			raise ValueError(('Superuser must have is_staff=True'))
		if extra_fields.get("is_superuser") is not True:
			raise ValueError(('Superuser must have is_superuser=True'))
		
		return self.create_user(email, username, password, **extra_fields)

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
	id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
	email = models.EmailField('email address', unique=True)
	username = models.CharField(max_length=150)
	date_created = models.DateTimeField(default=timezone.now)

	objects = UserManager()

	@property
	def is_staff(self):
		return self.is_superuser

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	def __str__(self):
		return self.username