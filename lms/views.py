from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.viewsets import ModelViewSet

from lms.models import Course, Lesson
from lms.serializers import CourseSerializer, LessonSerializer


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
