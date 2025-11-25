from django.contrib import admin
from .models  import Post,Author,Tag,Comment



class AdminDisplay(admin.ModelAdmin):
     list_filter= ("author","tags","date",)
     list_display= ("title","date","author",)
     prepopulated_fields = {"slug": ("title",)}

class CommentAdminClass(admin.ModelAdmin):
     list_display = ("user_name","user_email","text",)
     list_filter = ("user_email","user_name","text",)

admin.site.register(Post,AdminDisplay)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment)