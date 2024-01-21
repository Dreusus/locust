# Locust

## Установка

Для работы с проектом убедитесь, что у вас установлен Python версии 3.6 или выше.
Установите Locust с помощью следующей команды:

```bash
pip install locust
pip install locust-plugins

```

## Запуск тестов с веб-интерфейсом

```bash
locust
```

## Запуск тестов в фоновом режиме

Для запуска тестов в фоновом режиме и сохранения результатов в HTML-отчет, используйте следующую команду:

Для Windows (PowerShell)

```bash
locust -f locustfile.py --headless -u 10 -r 10 -t 20s --html="reports/report_$(Get-Date -Format "yyyyMMdd_HHmmss").html"
```

Для Unix/Linux/macOS

```bash
locust -f locustfile.py --headless -u 10 -r 10 -t 20s --html=reports/report_$(date +"%Y%m%d_%H%M%S").html
```

