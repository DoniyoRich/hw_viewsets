from django.contrib import admin

from users.models import CustomUser, Payment


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "avatar", "phone_number", "city")
    list_filter = ("email", "city",)
    search_fields = ("email", "city")


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "client", "date_paid", "amount")
    list_filter = ("id", "client", "date_paid", "amount")
    search_fields = ("id", "client", "date_paid", "amount")
