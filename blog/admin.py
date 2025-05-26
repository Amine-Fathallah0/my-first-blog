from django.contrib import admin
from .models import Post
class AdminAuthor(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date', 'published_date')
    search_fields = ('title', 'author__username')
    list_filter = ('published_date', 'author')
    


admin.site.register(Post, AdminAuthor)
