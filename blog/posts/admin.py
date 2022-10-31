from django.contrib import admin
from .models import Post, Comment
# Register your models here.
admin.site.register(Post)
#we can register models with  a decorator as well https://docs.djangoproject.com/en/4.1/ref/contrib/admin/
@admin.register(Comment)

# the CommentAdmin class customizes the representation of data on the screen
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)