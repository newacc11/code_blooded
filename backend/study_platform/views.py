from django.db.models import Q
from django.shortcuts import render, redirect

from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from . import models


class UserIsTeacher(UserPassesTestMixin):
    def test_func(self):
        check = False
        if not self.request.user.is_anonymous:
            try:
                check = self.request.user.userprofile.type == 'teacher'
            except:
                pass
        return check

    def handle_no_permission(self):
        if self.request.user.is_anonymous:
            return redirect('login')
        else:
            return redirect('main')


class IsStudentsTask(UserPassesTestMixin):
    def test_func(self):
        check = False
        if not self.request.user.is_anonymous:
            try:
                # check = self.request.user.userprofile.type == 'teacher'
                #TODO: записать в check True если задача доступна ученику
                pass

            except:
                pass
        return check

    def handle_no_permission(self):
        if self.request.user.is_anonymous:
            return redirect('login')
        else:
            return redirect('main')


class MainPage(ListView, LoginRequiredMixin):
    model = models.Contest
    template_name = 'study_program/main.html'

    #TODO: сделать передачу в context: задач без

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.userprofile.type == 'teacher':
            # TODO: проверить вывод
            return queryset.filter(teacher=self.request.user)
        else:
            student_filter_val = [self.request.user.pk]
            student_classes_ids = []
            for student_class in models.Class.objects.filter(students__in=student_filter_val):
                student_classes_ids.append(student_class.pk)
            return queryset.filter(
                Q(students__in=student_filter_val) | Q(classes__in=student_classes_ids)
            )


class TaskDetailView(DetailView, LoginRequiredMixin):
    model = models.Task
    # TODO: проверить вывод конкретной задачи, если нет, то допилить



