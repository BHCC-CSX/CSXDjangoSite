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
    path('index/', views.project_index, name="project_index"),
    path('<int:pk>/', views.project_detail, name="project_detail"),
    path('proposal/', views.project_proposal, name="project_proposal"),
    path('proposal_confirm/', views.project_proposal_confirm,
         name="project_proposal_confirm")
]

urlpatterns.extend(router.urls)
