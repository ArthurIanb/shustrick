from django.contrib import admin
from .models import Article, Comment

class ArticleAdmin(admin.ModelAdmin):
    list_display = 'pk', 'title', 'is_published', 'creator'

class CommentAdmin(admin.ModelAdmin):
    readonly_fields = 'created', 
    list_display = 'sender', 'data', 'article', 'created'

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)