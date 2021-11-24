from django.contrib import admin

# Register your models here.

from .models import Category, Job

admin.site.register(Job)
admin.site.register(Category)