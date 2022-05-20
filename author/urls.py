from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.get_all_authors, name="all_author_url")
]