from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Todo(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=30000)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=False, null=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE,null=True)
    objects = models.Manager()

    class Meta:
        app_label = 'todo_list'

    def __str__(self):
        return self.title
