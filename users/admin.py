from django.contrib import admin
from .models import Department, User, Rank, UserType

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_name', 'initials')
    search_fields = ['department_name']

class UserAdmin(admin.ModelAdmin):
    list_display = ('service_number', 'rank', 'name', 'contact', 'email', 'department', 'usertype', 'password')
    search_fields = ['service_number', 'rank', 'name', 'contact', 'email', 'department', 'usertype', 'password']

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
