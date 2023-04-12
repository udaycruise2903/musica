from django.urls import path

from . import views

urlpatterns = [
    path("", views.search, name="search"),
    path("search/<str:query>/", views.search_results, name="search_results"),
]
