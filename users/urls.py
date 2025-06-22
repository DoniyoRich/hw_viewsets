from django.urls import path

from users.apps import UsersConfig
from users.views import PaymentsListAPiView, PaymentUpdateAPIView

app_name = UsersConfig.name

urlpatterns = [
    path("payments/", PaymentsListAPiView.as_view(), name="payments"),
    path("payments/update/<int:pk>/", PaymentUpdateAPIView.as_view(), name="payment-update"),
]
