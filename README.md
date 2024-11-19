# django_shop

## Запуск задачи в фоновом режиме

```commandline
celery -A conf worker -l info -P gevent
```

## Запуск задачи по расписанию

```commandline
celery -A conf beat -l info
```
