from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager
from django.db.models import signals

"""

class UserProfile(models.Model):
	user = models.OneToOneField(User, unique=True)
	first_name = models.CharField(max_length=30, null=False, blank=False)
	last_name = models.CharField(max_length=30, null=False, blank=False)
	school_name = models.CharField(max_length=50, null=True, blank=True)
	email = models.EmailField(max_length=60, null=True, blank=True)
	student_id = models.BigIntegerField(null=True, blank=True)

def create_profile(sender, instance, created, **kwargs):
	if created:
		profile, created = UserProfile.\
			objects.get_or_create(user=instance)

signals.post_save.connect(create_profile, sender=User)

"""

#User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

class MyUserManager(BaseUserManager):

    def create_user(self, username, email, first_name, last_name, school_name, student_id, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
        	username=username,
			email=MyUserManager.normalize_email(email),
        	first_name=first_name,
        	last_name=last_name,
        	school_name=school_name,
            student_id = student_id,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        u = self.create_user(username,
                        password=password,
                        date_of_birth=date_of_birth
                    )
        u.is_admin = True
        u.save(using=self._db)
        return u


class Student(AbstractBaseUser):
	email = models.EmailField(
                        verbose_name='email address',
                        max_length=255,
                        unique=True,
                    )
	username = models.CharField(max_length=30, null=False, blank=False, unique=True)
	first_name = models.CharField(max_length=30, null=False, blank=False)
	last_name = models.CharField(max_length=30, null=False, blank=False)
	school_name = models.CharField(max_length=50, null=True, blank=True)
	student_id = models.BigIntegerField(null=True, blank=True)

	is_admin = models.BooleanField(default=False)

	objects = MyUserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']