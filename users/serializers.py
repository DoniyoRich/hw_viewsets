from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from lms.models import Course, Lesson
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

    course_paid = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    lesson_paid = serializers.PrimaryKeyRelatedField(
        queryset=Lesson.objects.all(),
        required=False,
        allow_null=True
    )

    class Meta:
        model = Payment
        # fields = ("id", "course_paid", "lesson_paid", "amount", "date_paid", "type", "link_to_payment")
        fields = "__all__"
        extra_kwargs = {
            'client': {'required': False}
        }

    def validate(self, data):
        if not data.get('course_paid') and not data.get('lesson_paid'):
            raise serializers.ValidationError("Укажите курс или урок.")
        return data
