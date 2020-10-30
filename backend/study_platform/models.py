from django.db import models
from annoying.fields import AutoOneToOneField, JSONField
from django.contrib.auth.models import User


class UserProfile(models.Model):

    USERS_TYPES = (
        ('student', 'student'),
        ('teacher', 'teacher'),
    )

    user = AutoOneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=40, null=True, blank=True)
    type = models.CharField(choices=USERS_TYPES, max_length=30)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    point = models.PositiveIntegerField(default=0)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ('registration_date', )

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.user.username
        super().save(*args, **kwargs)


class Group(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="groups_teacher")
    students = models.ManyToManyField(User, blank=True, related_name="groups_students")
    title = models.CharField(max_length=300)
    description = models.TextField()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Учебная группа"
        verbose_name_plural = "Учебные группы"


class Curse(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="curses_teacher")
    students = models.ManyToManyField(User, blank=True, related_name="curses_students")
    groups = models.ManyToManyField(Group, blank=True)
    title = models.CharField(max_length=300)
    description = models.TextField()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Task(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    curse = models.ForeignKey(Curse, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.TextField()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"


class Condition(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Условие"
        verbose_name_plural = "Условия"


class Check(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    response = JSONField(null=True, blank=True, max_length=1000)
    answer = models.TextField()
    max_points = models.PositiveIntegerField(default=1)
    received_points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.student.userprofile.username} - {self.task.title} [{self.received_points} / {self.max_points}]"

    class Meta:
        verbose_name = "Решение"
        verbose_name_plural = "Решения"