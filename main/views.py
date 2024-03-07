from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, TemplateView

from main.forms import (
    FacultyModelForm,
    DepartmentModelForm,
    DirectionModelForm, GroupModelForm, PracticePlaceModelForm, UserModelForm
)
from main.models import (
    FacultyModel,
    DepartmentModel,
    DirectionModel,
    PracticePlaceModel,
    GroupModel, UserModel
)


class AdminView(TemplateView):
    template_name = 'admin.html'


class FacultyListView(ListView):
    template_name = 'faculties.html'
    queryset = FacultyModel.objects.order_by('-pk')
    context_object_name = 'faculties'


class FacultyCreateView(CreateView):
    model = FacultyModel
    template_name = 'faculty_create.html'
    form_class = FacultyModelForm

    def form_valid(self, form):
        return super(FacultyCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('main:admin')


class DepartmentListView(DetailView):
    model = FacultyModel
    template_name = 'departments.html'

    def get_context_data(self, **kwargs):
        context = super(DepartmentListView, self).get_context_data(**kwargs)
        faculty_instance = self.get_object()
        context['departments'] = faculty_instance.departments.all()
        return context


class DepartmentCreateView(CreateView):
    model = DepartmentModel
    template_name = 'department_create.html'
    form_class = DepartmentModelForm

    def get_context_data(self, **kwargs):
        context = super(DepartmentCreateView, self).get_context_data(**kwargs)
        context['faculties'] = FacultyModel.objects.all()
        return context

    def form_valid(self, form):
        return super(DepartmentCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('main:admin')


class DirectionsListView(DetailView):
    model = DepartmentModel
    template_name = 'directions.html'

    def get_context_data(self, **kwargs):
        context = super(DirectionsListView, self).get_context_data(**kwargs)
        department_instance = self.get_object()
        context['directions'] = department_instance.directions.all()
        return context


class DirectionCreateView(CreateView):
    model = DirectionModel
    template_name = 'direction_create.html'
    form_class = DirectionModelForm

    def get_context_data(self, **kwargs):
        context = super(DirectionCreateView, self).get_context_data(**kwargs)
        context['departments'] = DepartmentModel.objects.all()
        return context

    def form_valid(self, form):
        return super(DirectionCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('main:admin')


class PracticePlacesListView(DetailView):
    model = DirectionModel
    template_name = 'practice_places.html'

    def get_context_data(self, **kwargs):
        context = super(PracticePlacesListView, self).get_context_data(**kwargs)
        direction_instance = self.get_object()
        context['places'] = direction_instance.practice_places.all()
        return context


class GroupCreateView(CreateView):
    model = GroupModel
    template_name = 'group_create.html'
    form_class = GroupModelForm

    def get_context_data(self, **kwargs):
        context = super(GroupCreateView, self).get_context_data(**kwargs)
        context['directions'] = DirectionModel.objects.all()
        return context

    def form_valid(self, form):
        return super(GroupCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('main:admin')


class PracticePlaceCreateView(CreateView):
    model = PracticePlaceModel
    template_name = 'practice_create.html'
    form_class = PracticePlaceModelForm

    def get_context_data(self, **kwargs):
        context = super(PracticePlaceCreateView, self).get_context_data(**kwargs)
        context['directions'] = DirectionModel.objects.all()
        return context

    def form_valid(self, form):
        return super(PracticePlaceCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('main:admin')


class UsersListView(DetailView):
    model = PracticePlaceModel
    template_name = 'practice_place.html'

    def get_context_data(self, **kwargs):
        context = super(UsersListView, self).get_context_data(**kwargs)
        place_instance = self.get_object()
        context['users'] = place_instance.users.all()
        return context


class UserCreateView(CreateView):
    pass