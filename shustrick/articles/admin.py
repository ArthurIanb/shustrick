from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = 'title', 'is_published', 'creator'


admin.site.register(Article, ArticleAdmin)
