from django.views.generic import CreateView, UpdateView, View
from todo_list.models import Todo
from django.urls import reverse_lazy, reverse
from todo_list.forms import TodoCreationForm, SignUpForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect


class TodoCreateView(LoginRequiredMixin, CreateView):
    login_url = '/todo_list/todologin'
    form_class = TodoCreationForm
    template_name = 'todo_list/todo_list.html'
    success_url = reverse_lazy('todo_create')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner = self.request.user
        obj.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('todo_list:todo_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Todo.objects.filter(owner=self.request.user)
        return context


class SignUpPage(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('todo_login')
    template_name = 'todo_list/todo_signup.html'


class LoginPage(SuccessMessageMixin, LoginView):
    template_name = 'todo_list/todo_login.html'
    success_message = "You are successfully logged in!"


class LogoutPage(LogoutView):
    def get_next_page(self):
        next_page = super(LogoutPage, self).get_next_page()
        messages.add_message(
            self.request, messages.SUCCESS,
            'You successfully logged out!'
        )
        return reverse('todo_list:todo_create')


class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['title', 'desc']
    template_name_suffix = '_update'
    success_url = reverse_lazy('todo_list:todo_create')


class TodoDeleteView(View):
    def get(self, request, pk):
        obj = Todo.objects.get(pk=pk)
        obj.delete()
        return redirect(reverse('todo_list:todo_create'))
