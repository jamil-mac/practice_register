from django import forms

from main.models import FacultyModel, DepartmentModel, DirectionModel, GroupModel, PracticePlaceModel, UserModel


class FacultyModelForm(forms.ModelForm):
    class Meta:
        model = FacultyModel
        fields = ('faculty_name', 'abbreviation',)


class DepartmentModelForm(forms.ModelForm):
    class Meta:
        model = DepartmentModel
        fields = ('dep_name', 'abbreviation', 'faculty',)


class DirectionModelForm(forms.ModelForm):
    class Meta:
        model = DirectionModel
        fields = ('direction_name', 'abbreviation', 'department')


class GroupModelForm(forms.ModelForm):
    class Meta:
        model = GroupModel
        fields = ('number', 'direction',)


class PracticePlaceModelForm(forms.ModelForm):
    class Meta:
        model = PracticePlaceModel
        fields = ('name', 'abbreviation', 'phone_number', 'address', 'target', 'direction',)


class UserModelForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'group', 'faculty', 'department', 'direction', 'practice_place',)
