from django.urls import path
from . import views

app_name = 'teacher'

urlpatterns = [
    # path('', views.MainPage.as_view(), name='main'), TODO: придумать что тут выводить
    path('contest/<pk>/', views.TasksListView.as_view(), name='contest_view'),
    path('task/<pk>/', views.TaskDetailView.as_view(), name='task_view'),
]
