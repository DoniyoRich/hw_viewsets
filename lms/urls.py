from django.urls import path
from rest_framework.routers import DefaultRouter

from lms.apps import LmsConfig
from lms.views import (CourseViewSet, LessonCreateAPIView, LessonDeleteAPIView,
                       LessonDetailAPIView, LessonListAPIView,
                       LessonUpdateAPIView, PaymentsListAPiView,
                       PaymentUpdateAPIView)

app_name = LmsConfig.name

router = DefaultRouter()
router.register(r"courses", CourseViewSet, basename="courses")

urlpatterns = [
    path("lessons/", LessonListAPIView.as_view(), name="lessons"),
    path("lessons/create/", LessonCreateAPIView.as_view(), name="lesson-create"),
    path("lessons/update/<int:pk>/", LessonUpdateAPIView.as_view(), name="lesson-update"),
    path("lessons/detail/<int:pk>/", LessonDetailAPIView.as_view(), name="lesson-detail"),
    path("lessons/delete/<int:pk>/", LessonDeleteAPIView.as_view(), name="lesson-delete"),

    path("payments/", PaymentsListAPiView.as_view(), name="payments"),
    path("payments/update/<int:pk>/", PaymentUpdateAPIView.as_view(), name="payment-update"),
]

urlpatterns += router.urls
