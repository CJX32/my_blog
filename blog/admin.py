from django.contrib import admin
from blog.models import Post,Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    tag_display = ('title', 'url', 'pub_date')

admin.site.register(Post,PostAdmin)
admin.site.register(Comment)