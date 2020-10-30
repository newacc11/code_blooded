from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from study_platform import models
from django.contrib.auth.mixins import LoginRequiredMixin
from study_platform.mixins import UserIsTeacher


class TasksListView(ListView, LoginRequiredMixin, UserIsTeacher):
    model = models.Task
    template_name = 'teacher/contest.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = models.Contest.objects.get(pk=self.kwargs.get('pk'))
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        pk = self.kwargs.get('pk')
        return queryset.filter(contest__pk=pk)


class TaskDetailView(DetailView, LoginRequiredMixin, UserIsTeacher):
    model = models.Task
    template_name = 'teacher/task.html'
    # TODO: проверить вывод конкретной задачи, если нет, то допилить