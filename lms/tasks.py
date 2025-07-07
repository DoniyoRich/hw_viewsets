from celery import shared_task


@shared_task
def some_task():
    print("Hello")
