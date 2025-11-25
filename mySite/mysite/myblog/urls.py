from django.urls import path,include

from . import views 
urlpatterns = [
    path("",views.StartingPageView.as_view(), name="starting-page"),
    path("posts/",views.AllPostsView.as_view(), name="all-posts" ),
    path("post/<slug:slug>/",views.SinglePostView.as_view(),name="post-details"),
    path("read-later",views.ReadLater.as_view(),name="read-later")
]
