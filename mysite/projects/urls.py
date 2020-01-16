from django.urls import path, include
from . import views

# urlpatterns = [
# 	path("", views.project_index, name="project_index"),
# 	path("<int:pk>/", views.project_detail, name="project_detail"),
# ]

urlpatterns = [
	path('api/project/', views.ProjectListCreate.as_view()),
	]