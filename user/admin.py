from django.contrib import admin

# Register your models here.
from user.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name','address', 'phone','city','country']

admin.site.register(UserProfile,UserProfileAdmin)