from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

class NewUserAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        if obj.image:
            print("wtf", obj.image.url)
            return mark_safe('<img src="{}" width=100px/>'.format(obj.image.url))
        return "nophoto"
    readonly_fields = "image_tag",
    fields = ["username", "password", "first_name", "email", "image_tag", "image"]
    list_display = ["image_tag", "username", "password", "first_name", "last_name", "email", "image"]

admin.site.register(User, NewUserAdmin)
