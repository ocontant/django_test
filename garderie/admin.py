from django.contrib import admin
from .models import Children, Parent, Educator, Classe

@admin.register(Children)
class ChildrenAdmin(admin.ModelAdmin):
	fieldsets = [
		('General Informations', {'fields': ["LastName", "FirstName", "Birthday"]}),
		#('Parent Info', {'fields': ['list_parents()']}),
		('Emergency Info', {'fields': ['RAMQ', 'RAMQ_Expiration']}),
	]

	#readonly_fields = ()

	def children_parents(self, obj):
			return obj.list_parents()
	
	children_parents.short_description = 'Parent(s)'
	
	list_display = ('LastName', 'FirstName','Birthday', 'children_parents')
	list_display_links = ('LastName','FirstName',)
	list_filter = ('LastName', 'FirstName',)
	search_fields = ['LastName', 'FirstName', 'Birthday', 'RAMQ',]

	
@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
	fieldsets = [
		('General Informations', {'fields': ["LastName", "FirstName", "Phone", "Email"]}),
		#('Children Info', {'fields': ['list_childrens()']}),
		('Emergency Info', {'fields': ['Phone_emergency']}),
	]

	#readonly_fields = ()

	def children_parents(self, obj):
			return obj.list_childrens()
		
	list_display = ('LastName', 'FirstName','Phone', 'Email',)
	list_display_links = ('LastName','FirstName',)
	list_filter = ('LastName', 'FirstName',)
	search_fields = ['LastName', 'FirstName', 'Phone', 'Email',]

	
@admin.register(Educator)
class EducatorAdmin(admin.ModelAdmin):
	fieldsets = [
		('General Informations', {'fields': ["LastName", "FirstName", "Phone", "Email"]}),
		#('Children Info', {'fields': ['list_classes()']}),
		('Emergency Info', {'fields': ['Phone_emergency']}),
	]

	#readonly_fields = ()

	def educator_classes(self, obj):
			return obj.list_classes()
		
	list_display = ('LastName', 'FirstName','Phone', 'Email',)
	list_display_links = ('LastName','FirstName',)
	list_filter = ('LastName', 'FirstName',)
	search_fields = ['LastName', 'FirstName', 'Phone', 'Email',]
	

@admin.register(Classe)
class ClasseAdmin(admin.ModelAdmin):
	fieldsets = [
		('General Informations', {'fields': ["Name"]}),
		#('Children Info', {'fields': ['list_classes()']}),
	]

	#readonly_fields = ()

	def classe_educators(self, obj):
			return obj.list_educators()
		
	list_display = ('Name',)
	list_display_links = ('Name',)
	list_filter = ('Name',)
	search_fields = ['Name',]
	