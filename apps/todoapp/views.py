from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
)
from apps.todoapp.forms import ToDoCreateForm
from apps.todoapp.models import ToDo


class ToDoListView(ListView):
    model = ToDo
    template_name = "ToDo/blog/index.html"
    context_object_name = 'post'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return ToDo.objects.all().filter(user=self.request.user)
        return []


class ToDoDetailView(DetailView):
    model = ToDo
    template_name = "ToDo/todo_detail.html"
    pk_url_kwarg = "pk"


class ToDoCreateView(CreateView):
    model = ToDo
    form_class = ToDoCreateForm
    template_name = "ToDo/todo_create.html"
    success_url = '/'
    context_object_name = 'post'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
