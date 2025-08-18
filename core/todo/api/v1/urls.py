from django.urls import path
from todo.api.v1 import views
from rest_framework.routers import DefaultRouter, SimpleRouter

app_name = "tasks_api"

# urlpatterns = [
#     path("", views.TaskListgenericView.as_view(), name="list"),
# ]
router = SimpleRouter()
router.register("task", views.TaskListgenericView, basename="task")
urlpatterns = router.urls