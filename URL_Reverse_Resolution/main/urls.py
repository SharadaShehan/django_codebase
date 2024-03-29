from django.urls import path
from . import views

app_name = "homepage"
urlpatterns = [
    path("first_view", views.first_view, name="main_view"),
    path("second_view", views.second_view, name="sub_view"),
    path("view/<slug:text>", views.view_with_path_parameters, name="param_view"),
]
