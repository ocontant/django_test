from django.db import models
from django.utils.timezone import now
from datetime import date, datetime
#from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Children(models.Model):
  #Children_ID = models.AutoField(primary_key=True)
  Parents = models.ManyToManyField('Parent')
  FirstName = models.CharField(max_length=40)
  LastName = models.CharField(max_length=40)
  Birthday = models.DateField()
  RAMQ = models.CharField(max_length=14, blank=True, null=True)
  RAMQ_Expiration = models.DateField(blank=True, null=True)
  
  # def save(self, *args, **kwargs):
    # if self.FullName is None:
      # self.FullName = self.LastName+" "+self.FirstName
      
    # super(Children, self).save(*args, **kwargs)
    
  def __str__(self):
    return self.FullName
  
  def list_parents(self):
    return ", ".join([parent.FullName for parent in self.Parents.all()])

  @property   
  def children_age(self):
    return int((date.today() - self.Birthday).days / 365.25  )
  
  @property
  def FullName(self):
    return self.LastName+" "+self.FirstName
    
    
class Parent(models.Model):
  #Parent_ID = models.AutoField(primary_key=True)
  FirstName = models.CharField(max_length=40)
  LastName = models.CharField(max_length=40)
  Email = models.EmailField()
  Phone = models.CharField(max_length=15)
  Phone_emergency = models.CharField(max_length=15)
  SIN = models.CharField(max_length=11)
  
  def __str__(self):
    return self.LastName + " " + self.FirstName
    
  def list_childrens(self, obj):
    return ", ".join([children.FullName for children in obj.children_set.all()])
  
  @property
  def FullName(self):
    return self.LastName+" "+self.FirstName
    
class Educator(models.Model):
  #Educator_ID = models.AutoField(primary_key=True)
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
  #Classe_ID = models.AutoField(primary_key=True)
  Educators = models.ManyToManyField(Educator)
  Name = models.CharField(max_length=255)

  
  def __str__(self):
    return "{} {}".format(self.Name, self.list_educators())

  def list_educators(self):
    return ", ".join([educator.name() for educator in self.Educators.all()])
    
    


    





    

