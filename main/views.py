from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from openpyxl.workbook import Workbook

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
    GroupModel,
    UserModel
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


def get_departments(request):
    faculty_id = request.GET.get('faculty_id')
    print(faculty_id)
    if faculty_id:
        departments = DepartmentModel.objects.filter(faculty_id=faculty_id)
        data = [{'id': department.id, 'name': department.dep_name} for department in departments]
        print(data)
        return JsonResponse({'departments': data})
    print('if did not work')
    return JsonResponse({})


def get_directions(request):
    department_id = request.GET.get('department_id')
    if department_id:
        directions = DirectionModel.objects.filter(department_id=department_id)
        data = [{'id': direction.id, 'name': direction.direction_name} for direction in directions]
        return JsonResponse({'directions': data})
    return JsonResponse({})


def get_practice_places(request):
    direction_id = request.GET.get('direction_id')
    if direction_id:
        practice_places = PracticePlaceModel.objects.filter(direction_id=direction_id)
        data = [{'id': place.id, 'name': place.name} for place in practice_places]
        return JsonResponse({'practice_places': data})
    return JsonResponse({})


def get_groups(request):
    direction_id = request.GET.get('direction_id')
    if direction_id:
        groups = GroupModel.objects.filter(direction_id=direction_id)
        data = [{'id': group.id, 'name': group.number} for group in groups]
        return JsonResponse({'groups': data})
    return JsonResponse({})


def user_create_view(request):
    form = UserModelForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return render(request, 'admin.html')

    faculties = FacultyModel.objects.all()

    context = {
        'form': form,
        'faculties': faculties
    }

    return render(request, 'register.html', context)


def export_data(request, pk):
    wb = Workbook()
    sheet = wb.active
    place = PracticePlaceModel.objects.get(pk=pk)
    users = place.users.all()

    sheet.append([place.name])
    sheet.title = str(place.name)
    sheet.append(['Ism', 'Familiya', 'Yo\'nalish', 'Guruh'])
    for user in users:
        sheet.append([user.first_name, user.last_name, user.direction.direction_name, user.group.number])

    filename = place.name

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename={filename}.xlsx'

    wb.save(response)

    return response
