from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'todo_list'
urlpatterns = [
    path('', TemplateView.as_view(template_name='todo_list/todo_home.html'), name='todo_home'),
    path('todocreate', views.TodoCreateView.as_view(), name='todo_create'),
    path('todoupdate/<int:pk>', views.TodoUpdateView.as_view(), name='todo_update'),
    path('tododelete/<int:pk>', views.TodoDeleteView.as_view(), name='todo_delete'),
    path('todosignup', views.SignUpPage.as_view(), name='todo_signup'),
    path('todologin', views.LoginPage.as_view(), name='todo_login'),
    path('todologout', views.LogoutPage.as_view(), name='todo_logout')
]
