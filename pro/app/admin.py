from django.contrib import admin
from .models import My_model

# Register your models here.
@admin.register(My_model)
class Admin(admin.ModelAdmin):
    list_display = ['id','name','email','password']