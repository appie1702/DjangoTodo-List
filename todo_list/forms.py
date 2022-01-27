from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm
from todo_list.models import Todo
from django.utils.translation import gettext_lazy as _
User = get_user_model()


class TodoCreationForm(ModelForm):
    title = forms.CharField(label='Title', min_length=2, max_length=150)
    desc = forms.CharField(label='Description', min_length=5, max_length=20000)
    class Meta:
        model = Todo
        fields = ['title', 'desc']
        widgets = {
            'name': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }
        error_messages = {
            'title': {
                'max_length': _("Title should be shorter")
            }
        }

class SignUpForm(UserCreationForm):
    username = forms.CharField(label='username', min_length=5, max_length=150)
    email = forms.EmailField(label='email')
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
    class Meta:
        model=User
        fields=[
            'username',
            'password'
        ]
