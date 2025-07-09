from celery import shared_task
from django.core.mail import send_mail
from celery.utils.log import get_task_logger
from django.utils import timezone

logger = get_task_logger(__name__)

from config.settings import DEFAULT_FROM_EMAIL
from users.models import CustomUser


@shared_task
def send_update_notification(course_id, course_title):
    """
    Отложенная задача отправки уведомлений об изменениях курса
    на e-mail адреса подписанных пользователей.
    """
    # сначала получаем список всех подписавшихся пользователей
    subscribed_users = CustomUser.objects.filter(
        subscriptions__course_id=course_id).values_list("email", flat=True)
    # subscribed_users = ["doniyor_ish@mail.ru", "donish1979@gmail.com"]
    logger.info(f"Отправка пользователям уведомлений об обновлении курса: {course_title}")
    print(subscribed_users)
    subject = f"Обновление курса:"
    message = f"""Уважаемый пользователь,\n
              Вышло обновление для курса: {course_title}.\n
              Добавилось много интересного.
              """
    if subscribed_users:
        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=DEFAULT_FROM_EMAIL,
                recipient_list=subscribed_users,
                fail_silently=False
            )
        except Exception as e:
            logger.error(f"Ошибка отправки уведомлений: {str(e)}")


@shared_task
def check_user_activity():
    """
    Задача запускается регулярно, проверяет всех пользователей в БД,
    и если кто-то ни разу не логинился или заходил более 30 дней назад,
    то этот пользователь блокируется.
    """
    users = CustomUser.objects.filter(is_active=True)
    today = timezone.now()
    no_active_period = 30  # в нашем случае это дни
    for user in users:
        if user.last_login is None or (today - user.last_login).days > no_active_period:
            user.is_active = False
            user.save()
