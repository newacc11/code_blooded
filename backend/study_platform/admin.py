from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from . import models


# Register your models here.


class UserProfileInline(admin.StackedInline):
    model = models.UserProfile
    max_num = 1
    can_delete = False


class UserAdmin(AuthUserAdmin):
    list_per_page = 500
    list_display = ('account_usernames', 'account_type', 'account_email')
    inlines = [UserProfileInline]

    @staticmethod
    def account_usernames(self):
        return self.userprofile.username

    @staticmethod
    def account_type(self):
        return self.userprofile.type

    @staticmethod
    def account_email(obj):
        return obj.userprofile.email


admin.site.unregister(models.User)
admin.site.register(models.User, UserAdmin)


class ContestAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Contest, ContestAdmin)


class TaskAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Task, TaskAdmin)


class TestAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Test, TestAdmin)


class CheckAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Check, CheckAdmin)


class ClassAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Class, ClassAdmin)

