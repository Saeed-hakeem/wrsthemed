from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm

from .models import Department, User, Rank, UserType

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_name', 'initials')
    search_fields = ['department_name']

class UserAdmin(admin.ModelAdmin):
    form = UserChangeForm
    model = User
    list_display = ('service_number', 'rank', 'name', 'contact', 'email', 'department', 'usertype')
    search_fields = ['service_number', 'name', 'email']

class RankAdmin(admin.ModelAdmin):
    list_display = ('rank_name', 'initials')
    search_fields = ['rank_name',]



class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('type_name', 'initials')
    search_fields = ['type_name', 'initials']



admin.site.register(Department, DepartmentAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Rank, RankAdmin)
admin.site.register(UserType, UserTypeAdmin)
