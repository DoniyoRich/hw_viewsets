from django.core.management import BaseCommand

from users.models import CustomUser


class Command(BaseCommand):
    """
    Команда для создания суперпользователя.
    """

    help = "Команда создания суперпользователя"

    def handle(self, *args, **options):
        su_email = input("Введите email суперпользователя: ")
        user = CustomUser.objects.create(email=su_email)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.set_password("123")
        user.save()
        print(f"Суперпользователь {su_email} создан успешно")
