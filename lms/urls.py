from django.urls import path
from rest_framework.routers import DefaultRouter

from lms.apps import LmsConfig
from lms.views import CourseViewSet, LessonListAPIView

app_name = LmsConfig.name

router = DefaultRouter()
router.register(r"courses/", CourseViewSet, basename="courses")

urlpatterns = [
    path("lessons/", LessonListAPIView.as_view(), name="lessons"),
    path("lessons/create", LessonListAPIView.as_view(), name="lesson-create"),
    path("lessons/update/<int:pk>", LessonListAPIView.as_view(), name="lesson-update"),
    path("lessons/detail/<int:pk>", LessonListAPIView.as_view(), name="lesson-detail"),
    path("lessons/delete/<int:pk>", LessonListAPIView.as_view(), name="lesson-delete"),
]

urlpatterns += router.urls
