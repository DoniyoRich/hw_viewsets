from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

from config.constants import PAYMENT_TYPES
from config.settings import AUTH_USER_MODEL
from lms.models import Course, Lesson

'''
class CustomUserManager(BaseUserManager):
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

    def _create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
'''

class CustomUser(AbstractUser):
    """
    Модель кастомного пользователя.
    """

    username = None
    email = models.EmailField(
        unique=True,
        verbose_name="e-mail"
    )
    avatar = models.ImageField(
        upload_to="users/avatars/",
        verbose_name="Аватар",
        blank=True, null=True
    )
    phone_number = models.CharField(
        max_length=30,
        verbose_name="Номер телефона",
        blank=True, null=True
    )
    city = models.CharField(
        max_length=50,
        verbose_name="Город",
        blank=True, null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    # objects = CustomUserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class Payment(models.Model):
    """
    Модель платежей.
    """
    client = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Плательщик")
    date_paid = models.DateField(verbose_name="Дата платежа")
    course_paid = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Оплаченный курс")
    lesson_paid = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="Оплаченный урок")
    amount = models.PositiveIntegerField(verbose_name="Сумма оплаты")
    type = models.CharField(max_length=30, choices=PAYMENT_TYPES, verbose_name="Способ оплаты")

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
        ordering = ["client", "date_paid", "amount"]

    def __str__(self):
        return f"Клиент {self.client}. Оплата - {self.type} на сумму {self.amount}."
