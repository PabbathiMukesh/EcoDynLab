from django.urls import path
from .views import (
	paper_list_view,
	paper_detail_view,
	paper_create_view,
)

from . import views
urlpatterns = [
    path('', views.index, name='index'),
	path('api/create/', paper_create_view),
	path('api/list/', paper_list_view),
	path('api/<int:paper_id>/', paper_detail_view),
	path('papers/', views.papers, name='papers')
]
