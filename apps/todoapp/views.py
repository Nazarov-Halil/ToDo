from django.forms import inlineformset_factory
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    DeleteView,
)
from apps.todoapp.forms import ToDoCreateForm

from apps.todoapp.models import ToDo


class ToDoListView(ListView):
    objects = None
    model = ToDo
    template_name = "ToDo/blog/index.html"
    context_object_name = 'post'


class ToDoDetailView(DetailView):
    model = ToDo
    template_name = "ToDo/todo_detail.html"
    pk_url_kwarg = "pk"


class ToDoCreateView(CreateView):
    model = ToDo
    form_class = ToDoCreateForm
    template_name = "ToDo/todo_create.html"
    success_url = '/'


