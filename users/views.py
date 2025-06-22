from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView, UpdateAPIView

from users.models import Payment
from users.serializers import PaymentSerializer


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
