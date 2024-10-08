# GROUPS URL.PY
from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path("", views.GroupListView.as_view(), name="all"),
    path("new/", views.GroupCreateView.as_view(), name="create"),
    path("posts/in/<slug>", views.GroupDetailView.as_view(), name="single"),
    path("join/<slug>/",views.JoinGroup.as_view(),name="join"),
    path("leave/<slug>/",views.LeaveGroup.as_view(),name="leave"),
]
