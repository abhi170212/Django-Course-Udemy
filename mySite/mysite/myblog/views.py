from datetime import date
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Post
# ==============================
# POSTS DATA
# ==============================
posts = [
  
]

# ==============================
# HELPER FUNCTION
# ==============================
def get_post_date(post):
    return post["date"]


# ==============================
# VIEWS
# ==============================
def starting_page(request):
    latest_posts=Post.objects.all().order_by("-date")[:3]
    # latest_posts = sorted(posts, key=get_post_date, reverse=True)[:3] #last three post lists 
    return render(request, "myblog/index.html", {
        "posts": latest_posts
    })

def all_posts(request):
    ordered_posts= Post.objects.all().order_by("-date")
    # ordered_posts = sorted(posts, key=get_post_date, reverse=True)
    return render(request, "myblog/all-posts.html", {
        "all_posts": ordered_posts
    })


#new function after the models
def post_details(request,slug):
    identified_post=(Post.objects.get(slug=slug))
    return render(request,"myblog/post-details.html",{
        "post":identified_post,
        "post_tags":identified_post.tags.all()
    })

# old function when we do not have the models in the file
# def post_details(request, slug):
#      identified_post = next((post for post in posts if post['slug'] == slug), None)
#      if identified_post is None:
#          raise Http404("Post not found")
#      return render(request, "myblog/post-details.html", {
#         "post": identified_post
#     })
     

# the identified post can be named as this too, 
# identified_post = None;
# for post in posts :
#     if post['slug'] == slug :
#         identified_post = post;
#         break;