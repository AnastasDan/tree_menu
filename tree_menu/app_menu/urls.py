from django.urls import path

from .views import IndexView

app_name = "tree_menu"

urlpatterns = [path("tree_menu/", IndexView.as_view(), name="index")]
