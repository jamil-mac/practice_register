from django.contrib import admin

from main.models import UserModel, FacultyModel, DepartmentModel, DirectionModel, GroupModel, PracticePlaceModel


@admin.register(FacultyModel)
class FacultyModelAdmin(admin.ModelAdmin):
    list_display = ['faculty_name', 'abbreviation']
    search_fields = ['faculty_name', 'abbreviation']
    list_filter = ['faculty_name']


@admin.register(DepartmentModel)
class DepartmentModelAdmin(admin.ModelAdmin):
    list_display = ['dep_name', 'abbreviation']
    search_fields = ['dep_name', 'abbreviation']
    list_filter = ['dep_name']


@admin.register(DirectionModel)
class DirectionModelAdmin(admin.ModelAdmin):
    list_display = ['direction_name', 'abbreviation']
    search_fields = ['direction_name', 'abbreviation']
    list_filter = ['direction_name']


@admin.register(GroupModel)
class GroupModelAdmin(admin.ModelAdmin):
    list_display = ['number']
    search_fields = ['number']
    list_filter = ['number']


@admin.register(PracticePlaceModel)
class PracticePlaceModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'abbreviation']
    search_fields = ['name', 'abbreviation']
    list_filter = ['name']


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'group']
    search_fields = ['first_name', 'last_name', 'group']
    list_filter = ['first_name', 'last_name', 'group']
