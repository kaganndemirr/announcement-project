# Django
from django.contrib.auth.models import BaseUserManager
from departments.models import Department


class UserManager(BaseUserManager):
    def _create_user(self, email, password, department=None, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')

        if not department:
            department = Department.objects.filter(d_code="-").first()
            if not department:
                department = Department(d_code="-", name="Bolumsugit  z")
                department.save()

        email = self.normalize_email(email)
        user = self.model(email=email, department=department, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)
