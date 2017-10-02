from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Children(models.Model):
	Children_ID = models.AutoField(primary_key=True)
	Parents = models.ManyToManyField('Parent', through='Parent_Children')
	FirstName = models.CharField(max_length=40)
	LastName = models.CharField(max_length=40)
	Birthday = models.DateField()
	RAMQ = models.CharField(max_length=14, blank=True, null=True)
	RAMQ_Expiration = models.DateField(blank=True, null=True)
		
	def __str__(self):
		return "{}  {}".format(self.LastName + " " + self.FirstName, self.list_parents())
	
	def list_parents(self):
		return ", ".join([parent.name() for parent in self.Parents.all()])
		
		
class Parent(models.Model):
	Parent_ID = models.AutoField(primary_key=True)
	#Childrens = models.ManyToManyField(Children, through='Parent_Children')
	FirstName = models.CharField(max_length=40)
	LastName = models.CharField(max_length=40)
	Email = models.EmailField()
	Phone = models.CharField(max_length=15)
	Phone_emergency = models.CharField(max_length=15)
	SIN = models.CharField(max_length=11)
	
	def __str__(self):
		return "{}  {}".format(self.LastName + " " + self.FirstName, self.list_childrens())
		
	def list_childrens(self):
		return ", ".join([children.name() for children in self.Childrens.all()])
	
	
class Parent_Children(models.Model):
	Parent = models.ForeignKey(Parent)
	Children = models.ForeignKey(Children)
		

class Educator(models.Model):
	Educator_ID = models.AutoField(primary_key=True)
	#Classes = models.ManyToManyField('Classe', through='Classe_Educator')
	FirstName = models.CharField(max_length=40)
	LastName = models.CharField(max_length=40)
	FullName = "%s %s" % (LastName, FirstName)
	Email = models.EmailField()
	Phone = models.CharField(max_length=15)
	Phone_emergency = models.CharField(max_length=15)
	
	def __str__(self):
		return "{} {}".format(self.LastName + " " + self.FirstName, self.list_classes())
	
	def list_classes(self):
		return ", ".join([classe.name() for classe in self.Classes.all()])	

		
class Classe(models.Model):
	Classe_ID = models.AutoField(primary_key=True)
	Educators = models.ManyToManyField(Educator, through='Classe_Educator')
	Name = models.CharField(max_length=255)

	
	def __str__(self):
		return "{} {}".format(self.Name, self.list_educators())

	def list_educators(self):
		return ", ".join([educator.name() for educator in self.Educators.all()])
		
		
class Classe_Educator (models.Model):
	Classe = models.ForeignKey(Classe)
	Educator = models.ForeignKey(Educator)
		
		


		





		

