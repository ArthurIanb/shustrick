from django.contrib import admin
from .models import Article, Comment

class ArticleAdmin(admin.ModelAdmin):
    list_display = 'title', 'is_published', 'creator'

class CommentAdmin(admin.ModelAdmin):
    list_display = 'sender', 'data', 'article'

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)