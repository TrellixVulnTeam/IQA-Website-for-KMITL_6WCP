from django.urls import path

from . import views


urlpatterns = [
    path('', views.all_programs, name='all_programs'),
    path('<int:program_id>/', views.program_detail, name='program_detail')
]
