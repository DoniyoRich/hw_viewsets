from rest_framework.serializers import ModelSerializer

from lms.serializers import CourseSerializer, LessonSerializer
from users.models import CustomUser, Payment


class UserSerializer(ModelSerializer):
    """
    Сериализатор для модели пользователя.
    """

    class Meta:
        model = CustomUser
        # fields = ("id", "email", "avatar", "phone_number", "city")
        fields = "__all__"


class UserSerializerLimited(ModelSerializer):
    """
    Сериализатор для модели пользователя, поля только id, email, avatar, city, phone.
    """

    class Meta:
        model = CustomUser
        fields = ("id", "email", "avatar", "phone_number", "city")


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
