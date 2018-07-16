from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.MainListView.as_view()),
]
