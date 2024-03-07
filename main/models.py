from django.db import models
from django.utils.translation import gettext_lazy as _


class FacultyModel(models.Model):
    faculty_name = models.CharField(max_length=255, verbose_name=_('faculty_name'), db_index=True)
    abbreviation = models.CharField(max_length=30, verbose_name=_('abbreviation'), null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.faculty_name

    class Meta:
        verbose_name = _('faculty')
        verbose_name_plural = _('faculties')


class DepartmentModel(models.Model):
    dep_name = models.CharField(max_length=255, verbose_name=_('dep_name'), db_index=True)
    abbreviation = models.CharField(max_length=30, verbose_name=_('abbreviation'), null=True, blank=True)
    faculty = models.ForeignKey(
        FacultyModel,
        on_delete=models.CASCADE,
        related_name='departments',
        verbose_name=_('faculty')
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.dep_name

    class Meta:
        verbose_name = _('department')
        verbose_name_plural = _('departments')


class DirectionModel(models.Model):
    direction_name = models.CharField(max_length=255, verbose_name=_('direction_name'), db_index=True)
    abbreviation = models.CharField(max_length=30, verbose_name=_('abbreviation'), null=True, blank=True)
    department = models.ForeignKey(
        DepartmentModel,
        on_delete=models.CASCADE,
        related_name='directions',
        verbose_name=_('department')
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.abbreviation

    class Meta:
        verbose_name = _('direction')
        verbose_name_plural = _('directions')


class GroupModel(models.Model):
    number = models.CharField(max_length=5, verbose_name=_('number'), db_index=True)
    direction = models.ForeignKey(
        DirectionModel,
        on_delete=models.CASCADE,
        related_name='groups',
        verbose_name=_('direction')
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = _('group')
        verbose_name_plural = _('groups')


class PracticePlaceModel(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('name'), db_index=True)
    abbreviation = models.CharField(max_length=30, verbose_name=_('abbreviation'), null=True, blank=True)
    phone_number = models.CharField(max_length=13, verbose_name=_('phone_number'))
    address = models.CharField(max_length=255, verbose_name=_('address'))
    target = models.CharField(max_length=100, verbose_name=_('target'))
    direction = models.ForeignKey(
        DirectionModel,
        on_delete=models.CASCADE,
        related_name='practice_places',
        verbose_name=_('department')
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('practice place')
        verbose_name_plural = _('practice places')


class UserModel(models.Model):
    first_name = models.CharField(max_length=30, verbose_name=_('first_name'), db_index=True)
    last_name = models.CharField(max_length=30, verbose_name=_('last_name'))
    faculty = models.ForeignKey(
        FacultyModel,
        on_delete=models.CASCADE,
        related_name='students',
        verbose_name=_('faculty')
    )
    department = models.ForeignKey(
        DepartmentModel,
        on_delete=models.CASCADE,
        related_name='students',
        verbose_name=_('department')
    )
    direction = models.ForeignKey(
        DirectionModel,
        on_delete=models.CASCADE,
        related_name='students',
        verbose_name=_('direction')
    )
    group = models.ForeignKey(
        GroupModel,
        on_delete=models.CASCADE,
        related_name='students',
        verbose_name=_('group')
    )
    practice_place = models.ForeignKey(
        PracticePlaceModel,
        on_delete=models.CASCADE,
        related_name='users',
        verbose_name=_('practice_place')
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
