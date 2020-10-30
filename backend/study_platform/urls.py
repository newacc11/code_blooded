from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
    path('', views.MainPage.as_view(), name='main'),
    # path('student/task/<pk>/', views.MainPage.as_view(), name='s_task_view'),
    # path('student/contest/<pk>/', views.TasksListView.as_view(), name='s_contest_view'),
    path('login/', LoginView.as_view(
        template_name='study_program/registration/login.html',
        redirect_authenticated_user=True,
    ), name='login'),
    path('logout/', LogoutView.as_view(template_name='study_program/registration/logout.html'), name='logout'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
