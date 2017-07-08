from django.db import models

class IDUser(models.Model):
	user_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	pictureURL = models.CharField(max_length=400)
	date_of_birth = models.DateField()


class NewIDUser(models.Model):
	user_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	pictureURL = models.CharField(max_length=400)
	date_of_birth = models.DateField()