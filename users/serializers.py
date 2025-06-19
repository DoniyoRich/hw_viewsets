from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from lms.models import Course, Lesson
from users.models import CustomUser, Payment


class UserSerializer(ModelSerializer):
    """
    Сериализатор для модели пользователя.
    """

    class Meta:
        model = CustomUser
        fields = ("id", "email")


class LessonSerializer(ModelSerializer):
    """
    Сериализатор для модели урока.
    """

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    """
    Сериализатор для модели курса.
    """

    lessons_count = SerializerMethodField()
    lessons = LessonSerializer(many=True)

    class Meta:
        model = Course
        fields = "__all__"

    @staticmethod
    def get_lessons_count(course):
        """
        Дополнительное поле, вычисляет количество уроков на курсе.
        """
        return course.lessons.count()


class PaymentSerializer(ModelSerializer):
    """
    Сериализатор для модели платежей.
    """
    client = UserSerializer(read_only=True)

    course_paid = CourseSerializer()
    lesson_paid = LessonSerializer()

    class Meta:
        model = Payment
        fields = "__all__"
