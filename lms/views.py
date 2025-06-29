from django.shortcuts import get_object_or_404
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from lms.models import Course, Lesson, Subscription
from lms.paginators import LMSPaginator
from lms.serializers import (CourseSerializer, LessonSerializer,
                             SubscriptionSerializer)
from users.permissions import IsModerator, IsOwner


class CourseViewSet(ModelViewSet):
    """
    Вьюсет для CRUD операций по курсам.
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = LMSPaginator

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        """
        Модераторы могут смотреть и редактировать курсы, а создавать и удалять их не могут.
        """
        if self.action in ['list', 'retrieve', 'update', 'partial_update']:
            self.permission_classes = [IsModerator | IsOwner]
        elif self.action == 'create':
            self.permission_classes = [~IsModerator]
        elif self.action == 'destroy':
            self.permission_classes = [~IsModerator | IsOwner]
        return super().get_permissions()


class LessonListAPIView(ListAPIView):
    """
    API получения списка уроков.
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]
    pagination_class = LMSPaginator


class LessonCreateAPIView(CreateAPIView):
    """
    API создания урока.
    """
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModerator]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonUpdateAPIView(UpdateAPIView):
    """
    API редактирования урока.
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonDetailAPIView(RetrieveAPIView):
    """
    API получения одного урока.
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonDeleteAPIView(DestroyAPIView):
    """
    API удаления урока.
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwner | ~IsModerator]


class SubscriptionAPIView(CreateAPIView):
    """
    API создания/удаления подписки.
    """
    # queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def post(self, request, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get('course')
        course = get_object_or_404(Course, pk=course_id)
        subs_item = Subscription.objects.filter(user=user, course=course)

        if subs_item.exists():
            print(subs_item.exists())
            subs_item.delete()
            message = 'Подписка удалена'
        else:
            Subscription.objects.create(user=user, course=course)
            message = 'Подписка добавлена'
        return Response({'message': message})
