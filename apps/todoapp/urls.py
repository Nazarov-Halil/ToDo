from django.urls import path

from apps.todoapp.views import ToDoListView, ToDoDetailView, ToDoCreateView

urlpatterns = [
    path('', ToDoListView.as_view(), name="list_todo"),
    path('post/<int:pk>', ToDoDetailView.as_view(), name="detail_todo"),
    path('create/', ToDoCreateView.as_view(), name="create_post"),
]
