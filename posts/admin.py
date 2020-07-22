from django.contrib import admin
from .models import Post,Comment

admin.site.register(Comment)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display =(
        'id',
        'title',
        'content',
        'view_count',
        'created_at',
    )

    search_fields =(
        'title',
    )