from django.core.management.base import BaseCommand

from config.constants import TESTDATA_PAYMENTS
from users.models import Payment


class Command(BaseCommand):
    help = 'Заполняет таблицу платежей тестовыми данными'

    def handle(self, *args, **options):
        self.stdout.write("Начало заполнения данных...")

        try:
            for payment in TESTDATA_PAYMENTS:
                Payment.objects.create(**payment)
            self.stdout.write(self.style.SUCCESS('Данные успешно добавлены!'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ошибка: {e}'))
