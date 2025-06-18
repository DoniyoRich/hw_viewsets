from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.viewsets import ModelViewSet

from lms.models import Course, Lesson
from lms.serializers import (CourseSerializer, LessonSerializer,
                             PaymentSerializer)
from users.models import Payment


class CourseViewSet(ModelViewSet):
    """
    Вьюсет для CRUD операций по курсам.
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class LessonListAPIView(ListAPIView):
    """
    API получения списка уроков.
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonCreateAPIView(CreateAPIView):
    """
    API создания урока.
    """
    serializer_class = LessonSerializer


class LessonUpdateAPIView(UpdateAPIView):
    """
    API редактирования урока.
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDetailAPIView(RetrieveAPIView):
    """
    API получения одного урока.
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDeleteAPIView(DestroyAPIView):
    """
    API удаления урока.
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


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
