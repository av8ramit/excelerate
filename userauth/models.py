from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser

"""
class UserProfile(models.Model):
	user=models.ForeignKey(User,unique=True)
	middle_name = models.CharField(max_length=30, null=True, blank=True)
	first_name = models.CharField(max_length=30, null=False, blank=False)
	last_name = models.CharField(max_length=30, null=False, blank=False)
	school_name = models.CharField(max_length=50, null=True, blank=True)
	email = models.CharField(max_length=60, null=True, blank=True)
"""

class UserProfile(models.Model):
	user = models.OneToOneField(User, unique=True)
	middle_name = models.CharField(max_length=30, null=True, blank=True)
	first_name = models.CharField(max_length=30, null=False, blank=False)
	last_name = models.CharField(max_length=30, null=False, blank=False)
	school_name = models.CharField(max_length=50, null=True, blank=True)
	email = models.EmailField(max_length=60, null=True, blank=True)
	student_id = models.BigIntegerField(null=True, blank=True)

	def create_profile(sender, instance, created, **kwargs):
		if created:
			profile, created = UserProfile.\
				objects.get_or_create(user=instance)
				
	post_save.connect(create_profile, sender=User)