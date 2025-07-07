from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import AllowAny

from users.models import CustomUser, Payment
from users.permissions import IsModerator, IsOwner
from users.serializers import (PaymentSerializer, UserSerializer,
                               UserSerializerLimited)
from users.services import (create_stripe_price, create_stripe_product,
                            create_stripe_session)


class UserRegisterView(CreateAPIView):
    """
    API регистрации пользователя.
    """
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]

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
    permission_classes = [IsModerator]


class UserDetailAPIView(RetrieveAPIView):
    """
    API получения одного пользователя.
    """
    serializer_class = UserSerializerLimited
    queryset = CustomUser.objects.all()
    permission_classes = [IsModerator | IsOwner]


class UserUpdateAPIView(UpdateAPIView):
    """
    API редактирования профиля пользователя.
    """
    serializer_class = UserSerializerLimited
    queryset = CustomUser.objects.all()
    permission_classes = [IsOwner]


class UserDeleteAPIView(DestroyAPIView):
    """
    API удаления профиля пользователя.
    """
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [IsModerator]


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


class PaymentCreateAPIView(CreateAPIView):
    """
    API созания ссылки для платежа.
    """
    serializer_class = PaymentSerializer
    # queryset = Payment.objects.all()

    def perform_create(self, serializer):
        payment = serializer.save(client=self.request.user)
        product_id = create_stripe_product(payment)
        price = create_stripe_price(payment.amount, product_id)
        session_id, link_to_payment = create_stripe_session(price)
        payment.session_id = session_id
        payment.link_to_payment = link_to_payment
        payment.save()


class PaymentUpdateAPIView(UpdateAPIView):
    """
    API редактирования платежа.
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
