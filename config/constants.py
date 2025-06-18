from django.utils import timezone

PAYMENT_TYPES = (
    ('cash', 'Наличные'),
    ('transfer', 'Перевод на счет'),
)

TESTDATA_PAYMENTS = [
    {'client_id': 1, 'date_paid': timezone.now().date(), 'course_paid_id': 1, 'lesson_paid_id': 1, 'amount': 65000,
     'type': "Наличные"},
    {'client_id': 2, 'date_paid': timezone.now().date(), 'course_paid_id': 2, 'lesson_paid_id': 1, 'amount': 90000,
     'type': "Перевод на счет"},
    {'client_id': 3, 'date_paid': timezone.now().date(), 'course_paid_id': 4, 'lesson_paid_id': 3, 'amount': 80000,
     'type': "Перевод на счет"},
    {'client_id': 4, 'date_paid': timezone.now().date(), 'course_paid_id': 2, 'lesson_paid_id': 5, 'amount': 100000,
     'type': "Наличные"}
]
