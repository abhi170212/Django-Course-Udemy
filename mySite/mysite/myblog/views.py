from datetime import date
from django.shortcuts import render, get_object_or_404
from django.http import Http404,HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.views import View



from .forms import CommentForm
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

# functional view and below is the class view of this fucntion view
def starting_page(request):
    latest_posts=Post.objects.all().order_by("-date")[:3]
    # latest_posts = sorted(posts, key=get_post_date, reverse=True)[:3] #last three post lists 
    return render(request, "myblog/index.html", {
        "posts": latest_posts
    })

class StartingPageView(ListView):
    template_name="myblog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data




# def all_posts(request):
#     ordered_posts= Post.objects.all().order_by("-date")
#     # ordered_posts = sorted(posts, key=get_post_date, reverse=True)
#     return render(request, "myblog/all-posts.html", {
#         "all_posts": ordered_posts
#     })

class AllPostsView(ListView):
    template_name ="myblog/all-posts.html"
    model=Post
    ordering=["-date"]
    context_object_name="all_posts"





#new function after the models

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

# def post_details(request,slug):
#     identified_post=(Post.objects.get(slug=slug))
#     return render(request,"myblog/post-details.html",{
#         "post":identified_post,
#         "post_tags":identified_post.tags.all()
#     })


class SinglePostView(View):

    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get("stored_posts")   

        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later = False
        
        return is_saved_for_later
    

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request, post.id)
        }
        return render(request, "myblog/post-details.html", context)


    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.posts = post
            comment.save()
            return HttpResponseRedirect(reverse("post-details", args=[slug]))

        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request, post.id)
        }
        return render(request, "myblog/post-details.html", context)

class ReadLater(View):

    def get(self, request):
        stored_posts = request.session.get("stored_posts")

        if not stored_posts:
            return render(request, "myblog/stored-posts.html", {
                "posts": [],
                "has_posts": False
            })

        posts = Post.objects.filter(id__in=stored_posts)

        return render(request, "myblog/stored-posts.html", {
            "posts": posts,
            "has_posts": True
        })


    def post(self, request):
        stored_posts = request.session.get("stored_posts", [])

        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
            
        else:
            stored_posts.remove(post_id)
        request.session["stored_posts"] = stored_posts
        return HttpResponseRedirect(reverse("read-later"))
    