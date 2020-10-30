from django.db.models import Q
from django.shortcuts import render, redirect

from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from . import models


class MainPage(ListView, LoginRequiredMixin):
    model = models.Contest
    template_name = 'study_program/main.html'

    #TODO: сделать передачу в context: задач без

    def get_queryset(self):
        queryset = super().get_queryset()

        # вывод контестов для учителя
        if self.request.user.is_authenticated and self.request.user.userprofile.type == 'teacher':
            # TODO: проверить вывод
            return queryset.filter(teacher=self.request.user)
        # вывод контестов для ученика
        if self.request.user.is_authenticated and self.request.user.userprofile.type == 'student':
            # TODO: проверить вывод
            student_filter_val = [self.request.user.pk]
            student_classes_ids = []
            for student_class in models.Class.objects.filter(students__in=student_filter_val):
                student_classes_ids.append(student_class.pk)
            return queryset.filter(
                Q(students__in=student_filter_val) | Q(classes__in=student_classes_ids)
            )
        # вывод контестов для всех
        else:
            return queryset.filter(is_public=True)
