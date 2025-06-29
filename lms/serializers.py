from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from lms.models import Course, Lesson, Subscription
from lms.validators import OnlyYouTubeValidator


class LessonSerializer(ModelSerializer):
    """
    Сериализатор для модели урока.
    """

    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [OnlyYouTubeValidator(field="video")]


class CourseSerializer(ModelSerializer):
    """
    Сериализатор для модели курса.
    """

    lessons_count = SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = "__all__"

    @staticmethod
    def get_lessons_count(course):
        """
        Дополнительное поле, вычисляет количество уроков на курсе.
        """
        return course.lessons.count()


class SubscriptionSerializer(ModelSerializer):
    """
    Сериализатор для модели подписки.
    """

    class Meta:
        model = Subscription
        fields = "__all__"
