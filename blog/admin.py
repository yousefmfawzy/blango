from django.contrib import admin
from blog.models import Post, Tag
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('slug', 'published_at')

# Registering both models
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)


