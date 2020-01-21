from rest_framework import routers
from .api import ProjectViewSet

from django.urls import path
from . import views

# urlpatterns = [
    # path('index/', views.project_index, name="project_index"),
    # path('<int:pk>/', views.project_detail, name="project_detail"),
# ]

router = routers.DefaultRouter()
router.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = [
    router.urls,
    path('index/', views.project_index, name="project_index"),
    path('<int:pk>/', views.project_detail, name="project_detail"),
]