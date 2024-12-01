# Проєкт FastAPI

Цей проєкт реалізовано з використанням FastAPI
## Вимоги

Перед початком переконайтеся, що у вас встановлено:
- Python 3.9 або новіший
- pip (менеджер пакетів Python)
- virtualenv (рекомендовано для ізоляції середовища)

## Встановлення

1. **Клонуйте репозиторій**  
   ```bash git clone https://github.com/your-username/your-repo.git cd your-repo```
2. **Створіть віртуальне середовище та активуйте його**
Linux/macOS:

```bash Copy code python3 -m venv env source env/bin/activate```

Windows:

```bash Copy code python -m venv env .\env\Scripts\activate```

3. **Встановіть залежності**

```bash Copy code pip install -r requirements.txt```

## Запуск сервера
1. **Переконайтесь, що середовище активоване**

```bash Copy code source env/bin/activate  # для Linux/macOS .\env\Scripts\activate  # для Windows```

2. **Запустіть сервер через FastAPI**
3. 
Використайте uvicorn для запуску сервера:

```bash Copy code uvicorn main:app --reload```
