from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "is_active", "created_at")
    list_filter = ("is_active", "created_at")
    search_fields = ("title", "content", "author__email")
    prepopulated_fields = {"slug": ("title",)}
