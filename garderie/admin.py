from django.contrib import admin
from .models import Children, Parent, Educator, Classe
from datetime import date, datetime

@admin.register(Children)
class ChildrenAdmin(admin.ModelAdmin):
  def children_age(self, obj):
    return obj.children_age
        
  def children_parents(self, obj):
      return obj.list_parents()
  
  children_parents.short_description = 'Parent(s)'
  children_age.short_description = 'Age'
  
  fieldsets = [
    ('General Informations', {'fields': ['LastName', 'FirstName', 'Birthday', 'FullName', 'children_age']}),
    ('Parent Info', {'fields': ['Parents']}),
    ('Emergency Info', {'fields': ['RAMQ', 'RAMQ_Expiration']}),
  ]
  readonly_fields = ('FullName','children_age',)
  
  list_display = ('LastName', 'FirstName','Birthday', 'children_age', 'children_parents')
  list_display_links = ('LastName','FirstName',)
  list_filter = ('LastName', 'FirstName',)
  search_fields = ['LastName', 'FirstName', 'Birthday', 'RAMQ',]

  
@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
  def parent_childrens(self, obj):
    return obj.list_childrens(obj)
  
  parent_childrens.short_description = 'Children(s)'
  #readonly_fields = ()
  
  fieldsets = [
    ('General Informations', {'fields': ["LastName", "FirstName", "Phone", "Email"]}),
    #('Children Info', {'fields': ['Children.FullName']}),
    ('Emergency Info', {'fields': ['Phone_emergency']}),
  ]
  
  list_display = ('LastName', 'FirstName','Phone', 'Email','parent_childrens')
  list_display_links = ('LastName','FirstName',)
  list_filter = ('LastName', 'FirstName',)
  search_fields = ['LastName', 'FirstName', 'Phone', 'Email',]

  
@admin.register(Educator)
class EducatorAdmin(admin.ModelAdmin):
  def educator_classes(self, obj):
      return obj.list_classes()

  fieldsets = [
    ('General Informations', {'fields': ["LastName", "FirstName", "Phone", "Email"]}),
    #('Children Info', {'fields': ['list_classes()']}),
    ('Emergency Info', {'fields': ['Phone_emergency']}),
  ]

  #readonly_fields = ()
      
  list_display = ('LastName', 'FirstName','Phone', 'Email',)
  list_display_links = ('LastName','FirstName',)
  list_filter = ('LastName', 'FirstName',)
  search_fields = ['LastName', 'FirstName', 'Phone', 'Email',]
  

@admin.register(Classe)
class ClasseAdmin(admin.ModelAdmin):
  def classe_educators(self, obj):
      return obj.list_educators()
  
  fieldsets = [
    ('General Informations', {'fields': ["Name"]}),
    #('Children Info', {'fields': ['list_classes()']}),
  ]

  #readonly_fields = ()
  
  list_display = ('Name',)
  list_display_links = ('Name',)
  list_filter = ('Name',)
  search_fields = ['Name',]
  