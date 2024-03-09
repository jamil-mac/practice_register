from django.urls import path

from main.views import (
    FacultyListView,
    DepartmentListView,
    DirectionsListView,
    PracticePlacesListView,
    UsersListView,
    AdminView,
    FacultyCreateView,
    DepartmentCreateView,
    DirectionCreateView,
    GroupCreateView,
    PracticePlaceCreateView,
)

from main.views import (
    get_departments,
    get_directions,
    get_practice_places,
    get_groups,
    user_create_view
)

app_name = 'main'

urlpatterns = [
    path('get_departments/', get_departments, name='get_departments'),
    path('get_directions/', get_directions, name='get_directions'),
    path('get_practice_places/', get_practice_places, name='get_practice_places'),
    path('get_groups/', get_groups, name='get_groups'),
    path('register/', user_create_view, name='user_create_view'),

    path('admin/', AdminView.as_view(), name='admin'),

    path('faculties/', FacultyListView.as_view(), name='faculties'),
    path('faculties/create/', FacultyCreateView.as_view(), name='faculty-create'),

    path('department/<int:pk>/', DepartmentListView.as_view(), name='departments'),
    path('department/create/', DepartmentCreateView.as_view(), name='department-create'),

    path('direction/<int:pk>/', DirectionsListView.as_view(), name='directions'),
    path('direction/create/', DirectionCreateView.as_view(), name='direction-create'),

    path('practice_places/<int:pk>/', PracticePlacesListView.as_view(), name='places'),
    path('group/create/', GroupCreateView.as_view(), name='group-create'),

    path('practice_place/<int:pk>/', UsersListView.as_view(), name='users'),
    path('practice_place/create/', PracticePlaceCreateView.as_view(), name='practice-create'),

]
