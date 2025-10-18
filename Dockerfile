# Используем базовый образ Python
FROM python:3.12.1-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app


# Копируем зависимости проекта в контейнер
COPY requirements.txt /app/

# Устанавливаем зависимости проекта
# RUN pip install -r requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Копируем содержимое текущей директории в контейнер в /code
COPY . /app/

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

