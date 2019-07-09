from django.urls import path

from . import views  # from current folder, import views

urlpatterns = [
    path('new', views.new, name=''),
    path('', views.index, name=''),  # empty string in path means no specific filename, calls def index from views
    path('detail', views.detail, name='')
]