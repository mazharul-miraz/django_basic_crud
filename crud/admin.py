from django.contrib import admin
from  .models import studentInfo

# Register your models here.
@admin.register(studentInfo)
class studentAdmin(admin.ModelAdmin):
    list_display = ('name','email','address',)