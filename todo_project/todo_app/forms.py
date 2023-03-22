from .models import Task_todo
from django import forms


class TodoForm(forms.ModelForm):
    class Meta:
        model = Task_todo
        fields = ['name', 'priority', 'date']
