from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView

from users.models import Payment, CustomUser
from users.serializers import PaymentSerializer, UserSerializer, UserSerializerLimited


class UserRegisterView(CreateAPIView):
    """
    API регистрации пользователя.
    """
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(ListAPIView):
    """
    API получения списка пользователей.
    """
    serializer_class = UserSerializerLimited
    queryset = CustomUser.objects.all()


class UserDetailAPIView(RetrieveAPIView):
    """
    API получения одного пользователя.
    """
    serializer_class = UserSerializerLimited
    queryset = CustomUser.objects.all()


class UserUpdateAPIView(UpdateAPIView):
    """
    API редактирования профиля пользователя.
    """
    serializer_class = UserSerializerLimited
    queryset = CustomUser.objects.all()


class UserDeleteAPIView(DestroyAPIView):
    """
    API удаления профиля пользователя.
    """
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()


class PaymentsListAPiView(ListAPIView):
    """
    API отображения списка платежей.
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ('course_paid', 'lesson_paid', 'type')
    search_fields = ['type']
    ordering_fields = ['date_paid', ]


class PaymentUpdateAPIView(UpdateAPIView):
    """
    API редактирования платежа.
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
