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
    UserCreateView,
)

app_name = 'main'

urlpatterns = [
    path('admin/', AdminView.as_view(), name='admin'),
    path('', UserCreateView.as_view(), name='user-create'),

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
