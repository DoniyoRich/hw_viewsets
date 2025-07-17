# Домашнее задание "34.2 Docker Compose"
## Запуск проекта с помощью Docker Compose

## Предварительные требования
 - установленный Docker Desktop
 - файл .env с необходимыми переменными окружения (скопируйте из .env.example и настройте)

## Запуск проекта

### Соберите и запустите сервисы:

`docker-compose up -d --build`

При первом запуске создайте суперпользователя:

`python manage.py csu`

Авторизация в данном проекте происходит по email.

## Проверка работоспособности сервисов

Откройте в браузере: http://localhost:8000

### PostgreSQL (db):

`docker-compose exec db psql -U your_db_user -d your_db_name -c "\l"`

### Redis:

`docker-compose exec redis redis-cli ping`

Должен ответить "PONG"

### Celery Worker:
Проверьте логи на наличие ошибок:

`docker-compose logs celery`

### Celery Beat:
Проверьте логи:

`docker-compose logs beat`

### Полезные команды:
- Остановить все сервисы:

`docker-compose down`

- Перезапустить конкретный сервис (например, web):

`docker-compose restart web`

Просмотр логов определенного сервиса:

`docker-compose logs -f web`  # Логи Django

`docker-compose logs -f celery`  # Логи Celery worker


## Лицензия

[Doniyor Ishanov. ](#) - [SkyPro IT School](#)