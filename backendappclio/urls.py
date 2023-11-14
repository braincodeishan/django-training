# backendappclio/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello-world'),
    path('tables/', views.get_data, name='get-data'),
    path('addtodo/', views.addNewToDo, name="add-to-do"),
    path('show/', views.showTodoList, name="show-to-do-list"),
    path('deltodo/<int:todo_id>/', views.delTodo, name="delete_todo")
]
