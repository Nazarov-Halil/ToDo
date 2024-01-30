from django import forms
from apps.todoapp.models import ToDo


class ToDoCreateForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ('title', 'description',)
