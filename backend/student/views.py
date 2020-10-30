from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from study_platform import models


class TasksListView(ListView, LoginRequiredMixin):
    model = models.Task
    template_name = 'student/contest.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = models.Contest.objects.get(pk=self.kwargs.get('pk'))
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        pk = self.kwargs.get('pk')
        return queryset.filter(contest__pk=pk)


class TaskDetailView(DetailView, LoginRequiredMixin):
    model = models.Task
    template_name = 'student/task.html'
    # TODO: проверить вывод конкретной задачи, если нет, то допилить
