# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import (
	BaseUserManager, AbstractBaseUser, PermissionsMixin
)

# Local Django
from users.managers import UserManager



class User(AbstractBaseUser, PermissionsMixin):
	# Base
	first_name = models.CharField(verbose_name=_('First Name'), max_length=50)
	last_name = models.CharField(verbose_name=_('Last Name'), max_length=50)
	email = models.EmailField(
        verbose_name=_('Email'), max_length=255, blank=True, null=True,
		unique=True
    )
	department = models.ForeignKey(verbose_name=_('Department'), to='departments.Department',
		on_delete=models.CASCADE, null=True, blank=False
	)

	# Permisssions
	is_staff = models.BooleanField(verbose_name=('Staff'), default=False)
	is_active = models.BooleanField(verbose_name=_('Active'), default=True)
	is_verified = models.BooleanField(verbose_name=_('Verified'), default=False)

	objects = UserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name', 'last_name']


	class Meta:
		verbose_name = _('User')
		verbose_name_plural = _('Users')

	def __str__(self):
		return self.get_full_name()

	def get_full_name(self):
		return '{first_name} {last_name}'.format(first_name=self.first_name,
		last_name=self.last_name
	)
