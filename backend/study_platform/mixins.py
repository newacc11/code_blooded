from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect


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
