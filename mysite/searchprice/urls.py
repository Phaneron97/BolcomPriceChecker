from django.urls import path

from . import views  # from current folder, import views

urlpatterns = [
    path('', views.index, name='index'),  # empty string in path means no specific filename, calls def index from views
]