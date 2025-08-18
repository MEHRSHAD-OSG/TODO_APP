from django.urls import path, include
from . import views

app_name = "todo"

urlpatterns = [
    path("", views.TaskList.as_view(), name="task_list"),
    path("create/", views.TaskCreate.as_view(), name="create_task"),
    path("update/<int:pk>/", views.TaskUpdate.as_view(), name="update_task"),
    path("complete/<int:pk>/", views.TaskComplete.as_view(), name="complete_task"),
    path("undo/<int:pk>/", views.TaskUndo.as_view(), name="undo_task"),
    path("delete/<int:pk>/", views.TaskDeleteView.as_view(), name="delete_task"),
    path("api/v1/", include("todo.api.v1.urls")),
]
