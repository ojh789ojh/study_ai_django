from django.urls import path

from projectapp.views import ProjectCreationView, ProjectDetailView, ProjectListView

app_name = 'projectapp'

urlpatterns = [
    path('create/', ProjectCreationView.as_view(), name='create'),
    path('detail/<int:pk>', ProjectDetailView.as_view(), name='detail'),
    path('list/', ProjectListView.as_view(), name='list'),
]