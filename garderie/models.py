from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Children(models.Model):
	Children_ID = models.PositiveIntegerField(primary_key=True)
	FirstName = models.CharField(max_length=40)
	LastName = models.CharField(max_length=40)
	RAMQ = models.CharField(max_length=14, blank=True, null=True)
	RAMQ_Expiration = models.DateField(blank=True, null=True)
	Birthday = models.DateField()
	
	def __str__(self):
		return Children.__name__ + " " + self.FirstName + " " + self.LastName

		
class Parent(models.Model):
	Parent_ID = models.PositiveIntegerField(primary_key=True)
	Childrens = models.ManyToManyField(Children, through='Parent_Children', related_name='Children')
	FirstName = models.CharField(max_length=40)
	LastName = models.CharField(max_length=40)
	Email = models.EmailField()
	Phone = models.CharField(max_length=15)
	Phone_emergency = models.CharField(max_length=15)
	SIN = models.CharField(max_length=11)
	
	def __str__(self):
		return Parents.__name__ + " " + self.FirstName + " " + self.LastName
	

class Parent_Children(models.Model):
	Parent = models.ForeignKey(Parent)
	Children = models.ForeignKey(Children)

	def __str__(self):
		return self.Parent + " " + self.Children		
		

class Educator(models.Model):
	Educator_ID = models.PositiveIntegerField(primary_key=True)
	FirstName = models.CharField(max_length=40)
	LastName = models.CharField(max_length=40)
	Email = models.EmailField()
	Phone = models.CharField(max_length=15)
	Phone_emergency = models.CharField(max_length=15)
	
	def __str__(self):
		return Educator.__name__ + " " + self.FirstName + " " + self.LastName
		

class Classe(models.Model):
	Classe_ID = models.PositiveIntegerField(primary_key=True)
	Name = models.CharField(max_length=255)
	Educators = models.ManyToManyField(Educator, through='Classe_Educator', related_name='Educator')
	
	def __str__(self):
		return Classe.__name__ + " " + self.Name

		
class Classe_Educator (models.Model):
	Classe = models.ForeignKey(Classe)
	Educator = models.ForeignKey(Educator)
	
	
	def __str__(self):
		return self.Educator + " " + self.Classe
		
		


		





		

