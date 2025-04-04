# Используем официальный образ Python 3.11.7
FROM python:3.11.7-slim

# Устанавливаем зависимости системы
RUN apt-get update && apt-get install -y \
    && rm -rf /var/lib/apt/lists/*

# Создаём рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY . .

# Устанавливаем зависимости
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Запускаем бота
CMD ["python", "tg_bot.py"]