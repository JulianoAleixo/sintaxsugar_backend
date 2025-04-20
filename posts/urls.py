from django.urls import path

from .views import (
    PostCreateView,
    PostDeleteView,
    PostDetailView,
    PostListView,
    PostUpdateView,
    UpdatePostActiveStatusView,
)

urlpatterns = [
    path("", PostListView.as_view(), name="post-list"),
    path("create/", PostCreateView.as_view(), name="post-create"),
    path("<int:id>/", PostDetailView.as_view(), name="post-detail"),
    path("<int:id>/update/", PostUpdateView.as_view(), name="post-update"),
    path("<int:id>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("<int:id>/set-active/", UpdatePostActiveStatusView.as_view(), name="post-set-active"),
]
