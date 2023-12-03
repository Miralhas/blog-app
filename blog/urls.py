from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.PostList.as_view(), name="index"), # blog:index
    path("search/", views.SearchView.as_view(), name="search"),
    path("new_post", views.NewPostView.as_view(), name="new_post"),
    path("<slug:slug>/", views.PostDetail.as_view(), name="detail"),
    path("<slug:slug>/delete/", views.DeletePost.as_view(), name="delete_post"),
    path("<slug:slug>/edit/", views.EditPost.as_view(), name="edit_post"),
]