from django.urls import path
from . import views

urlpatterns = [
    path("todo/", views.TodoListCreate.as_view(), name="todo-list"),
    path("todo/update/<int:pk>", views.TodoUpdate.as_view(), name="todo-update"),
    path("todo/delete/<int:pk>", views.TodoDelete.as_view(), name="todo-delete")
]
