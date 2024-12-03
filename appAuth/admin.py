from django.contrib import admin

from appAuth.models import CustomUser


# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "user_type",
        "created_on",
        "updated_on",
        "is_deleted",
    )


admin.site.register(CustomUser, CustomUserAdmin)
