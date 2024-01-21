# Locust

## Установка

Для работы с проектом убедитесь, что у вас установлен Python версии 3.6 или выше.
Установите Locust с помощью следующей команды:

```bash
pip install locust
```

## Запуск тестов с веб-интерфейсом

```bash
locust
```

## Запуск тестов в фоновом режиме

```bash
locust -f locustfile.py --headless -u 10 -r 10 -t 20s --only-summary
```

