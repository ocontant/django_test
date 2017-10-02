from django.contrib import admin
from .models import Children, Parent, Educator, Classe

# Register your models here.
admin.site.register(Children)
admin.site.register(Parent)
admin.site.register(Educator)
admin.site.register(Classe)