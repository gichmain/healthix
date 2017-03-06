from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models


@python_2_unicode_compatible
class Doctor(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	mobile = models.CharField(max_length=200)
	date_of_birth = models.CharField(max_length=200)
	id_number = models.CharField(max_length=200)
	password = models.CharField(max_length = 200, default = 'doctor')

	def __str__(self):
		return "%s %s" % (self.first_name,self.last_name)
	


@python_2_unicode_compatible
class Patient(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	mobile = models.CharField(max_length=200)
	date_of_birth = models.CharField(max_length=200)
	id_number = models.CharField(max_length=200)

	def __str__(self):
		return "%s %s" % (self.first_name, self.last_name)


@python_2_unicode_compatible
class Laboratory(models.Model):
	lab_name = models.CharField(max_length = 200)
	mobile = models.CharField(max_length = 200)

	def __str__(self):
		return "%s laboratory" % self.lab_name
		


@python_2_unicode_compatible
class Session(models.Model):
	Session_type = models.CharField(max_length = 200)
	diagnosis = models.CharField(max_length = 200)
	date = models.DateTimeField('visitation day')
	patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
	lab = models.ForeignKey(Laboratory, on_delete = models.CASCADE)
	doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)

	def __str__(self):
		return ""


@python_2_unicode_compatible
class Laboratory_Test(models.Model):
	specimen = models.CharField(max_length = 200)
	lab_test = models.CharField(max_length = 600)
	duration = models.CharField(max_length = 100)
	result = models.CharField(max_length = 1200, default = 'pending')
	date_requested = models.DateTimeField('date requested')
	lab = models.ForeignKey(Laboratory, on_delete = models.CASCADE)
	doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
	patient = models.ForeignKey(Patient, on_delete = models.CASCADE)

	def __str__(self):
		return "specimen: %s <br>lab_test: %s" % (self.specimen, self.lab_test)


@python_2_unicode_compatible
class Laboratory_Technician(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	mobile = models.CharField(max_length=200)
	id_number = models.CharField(max_length=200)
	password = models.CharField(max_length = 200, default = 'laboratory')
	location = models.ForeignKey(Laboratory, on_delete = models.CASCADE)

	def __str__(self):
		return "%s %s" % (self.first_name,self.last_name)
	
		