from django.test import override_settings
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from lms.models import Course, Lesson
from users.models import CustomUser


@override_settings(
    REST_FRAMEWORK={
        'DEFAULT_AUTHENTICATION_CLASSES': [],
        'DEFAULT_PERMISSION_CLASSES': [],
    }
)
class LMSTestCase(APITestCase):
    """
    Класс тестирования уроков системы LMS.
    """

    def setUp(self):
        self.user = CustomUser.objects.create(email="admin@mail.com")

        self.course1 = Course.objects.create(title="Python разработчик",
                                             description="Курс о разработке на языке Python")
        self.course2 = Course.objects.create(title="Java разработчик", description="Курс о разработке на языке Java")
        self.course3 = Course.objects.create(title="C++ разработчик", description="Курс о разработке на языке C++")

        self.les1 = Lesson.objects.create(title="Введение в Python", description="Введение в Python",
                                          course=self.course1)
        self.les2 = Lesson.objects.create(title="Введение в Java", description="Введение в Java", course=self.course2)

    def test_get_list_lessons(self):
        """
        Тест на получение списка уроков.
        """
        self.client.force_authenticate(self.user)
        self.url = reverse("lms:lessons")
        response = self.client.get(self.url)
        total_lessons = Lesson.objects.all().count()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

        self.assertEqual(total_lessons, 2)

    def test_create_lesson(self):
        """
        Тест на создание урока.
        """
        self.client.force_authenticate(self.user)
        self.url = reverse("lms:lesson-create")
        self.data = {
            "title": "Списки и кортежи",
            "description": "Описание коллекций",
            "video": "http://youtube.com/newlesson",
            "course": self.course1.pk
        }
        response = self.client.post(self.url, self.data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )

    def test_create_lesson_no_youtube(self):
        """
        Тест на создание урока, при котором должен сработать валидатор
        на проверку вхождения ссылки на youtube.
        """
        self.client.force_authenticate(self.user)
        self.url = reverse("lms:lesson-create")
        self.data = {
            "title": "Списки и кортежи",
            "description": "Описание коллекций",
            "video": "http://yo.com/newlesson",
            "course": self.course1.pk
        }
        response = self.client.post(self.url, self.data)
        self.assertEqual(
            response.json(), {'non_field_errors': ['Ссылка ведет на другой ресурс, отличный от youtube.com']}
        )

    def test_detail_lesson(self):
        self.url = reverse("lms:lesson-detail", args=(self.les1.pk,))

        response = self.client.get(self.url)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

    def test_update_lesson(self):
        """
        Тест на обновление урока.
        """
        self.url = reverse("lms:lesson-update", args=(self.les1.pk,))
        self.data = {
            "title": "Циклы",
            "video": "http://youtube.com"
        }
        response = self.client.patch(self.url, self.data)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            response.json()["title"], "Циклы"
        )

    def test_delete_lesson(self):
        """
        Тест на удаление урока.
        """
        self.url = reverse("lms:lesson-delete", args=(self.les2.pk,))
        response = self.client.delete(self.url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )

    def test_subscription(self):
        self.client.force_authenticate(self.user)
        self.url = reverse("lms:subscription")

        # Добавляем подписку
        self.data = {
            "course": self.course1.id
        }
        response = self.client.post(self.url, self.data)
        print(response.json())
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            response.json()["message"], "Подписка добавлена"
        )

        # Удаляем подписку
        self.data = {
            "course": self.course1.id
        }
        response = self.client.post(self.url, self.data)
        print(response.json())
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            response.json()["message"], "Подписка удалена"
        )
