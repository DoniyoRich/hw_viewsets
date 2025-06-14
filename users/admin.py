from django.contrib import admin

from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "avatar", "phone_number", "city")
    list_filter = ("email", "city",)
    search_fields = ("email", "city")
