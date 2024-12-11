# Проєкт FastAPI

Цей проєкт реалізовано з використанням FastAPI
## Вимоги

Перед початком переконайтеся, що у вас встановлено:
- Python 3.9 або новіший
- pip (менеджер пакетів Python)
- virtualenv (рекомендовано для ізоляції середовища)

## Встановлення

1. **Клонуйте репозиторій**  
   ```https://github.com/your-username/your-repo.git cd your-repo```
2. **Створіть віртуальне середовище та активуйте його**
Linux/macOS:

```python3 -m venv env source env/bin/activate```

Windows:

```python -m venv env .\env\Scripts\activate```

3. **Встановіть залежності**

```pip install -r requirements.txt```

## Запуск сервера
1. **Переконайтесь, що середовище активоване**

```source env/bin/activate  # для Linux/macOS .\env\Scripts\activate  # для Windows```

2. **Запустіть сервер через FastAPI**

Використайте uvicorn для запуску сервера:

```uvicorn main:app --reload```
