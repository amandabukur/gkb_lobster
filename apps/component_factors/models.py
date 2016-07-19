from __future__ import unicode_literals

from django.db import models

class CategoryOption(models.Model):
	option = models.CharField(max_length=150, unique=True)
	def __str__(self):
		return self.option
	class Meta:
		ordering = ['option']

class ItemOption(models.Model):
	option = models.CharField(max_length=150, unique=True)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	requisites = models.ForeignKey(CategoryOption, verbose_name="Bike types that this feature is avalable for")

	def __str__(self):
		return self.option
	class Meta:
		ordering = ['option']


class HandlebarOption(models.Model):
	option = models.CharField(max_length=150, unique=True)
	price = models.DecimalField(max_digits=5, decimal_places=2)


	def __str__(self):
		return self.option

	class Meta:
		ordering = ['option']

class SaddleOption(models.Model):
	option = models.CharField(max_length=150, unique=True)
	price = models.DecimalField(max_digits=5, decimal_places=2)


	def __str__(self):
		return self.option

	class Meta:
		ordering = ['option']



