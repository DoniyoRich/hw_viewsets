from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import PaymentsListAPiView, PaymentUpdateAPIView, UserRegisterView, UserListAPIView, UserUpdateAPIView, \
    UserDetailAPIView, UserDeleteAPIView

app_name = UsersConfig.name

urlpatterns = [
    path("payments/", PaymentsListAPiView.as_view(), name="payments"),
    path("payments/update/<int:pk>/", PaymentUpdateAPIView.as_view(), name="payment_update"),

    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('register/', UserRegisterView.as_view(), name='register'),
    path('', UserListAPIView.as_view(), name='users_list'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
    path('detail/<int:pk>/', UserDetailAPIView.as_view(), name='user_detail'),
    path('delete/<int:pk>/', UserDeleteAPIView.as_view(), name='user_delete'),
]
