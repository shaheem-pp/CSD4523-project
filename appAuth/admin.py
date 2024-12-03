from django.contrib import admin
from django.utils.html import format_html

from appAuth.models import CustomUser


# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "thumbnail",
        "name",
        "email",
        "user_type",
        "created_on",
        "updated_on",
        "is_deleted",
    )

    def thumbnail(self, obj):
        return format_html(
            '<img src="{}" style="width: 2rem; height: 2rem; object-fit: contain;" />',
            (obj.image.url if obj.image else "/media/user/default.jpg"),
        )

    thumbnail.short_description = "Image"


admin.site.register(CustomUser, CustomUserAdmin)
