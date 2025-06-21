# telegram bot языковой студии ILT_school_bot

[![python](https://img.shields.io/badge/python-3.11-green)](https://img.shields.io/badge/python-3.11-green) [![aiogram](https://img.shields.io/badge/aiogram-3.0.0b7-green)](https://img.shields.io/badge/aiogram-3.0.0b7-green) [![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-green)](https://img.shields.io/badge/SQLAlchemy-2.0-green)

[![codewars](https://www.codewars.com/users/Kazykan/badges/small)](https://www.codewars.com/users/Kazykan/)

bot написан на aiogram 3.x & sqlalchemy 2.x

# Для работы
Нужен файл service_account.json переименовать service_account.json.common получить его можно на сайте https://console.developers.google.com/project
```sh
{
  "type": "service_account",
  "project_id": "",
  "private_key_id": "b",
  "private_key": "-----BEGIN PRIVATE",
  "client_id": "",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "",
  "client_x509_cert_url": ""
}
```

Создайте файл .env
```
ADMIN_TELEGRAM_ID=123456
TELEGRAM_TOKEN = '45648120:A56451235-XN65146131518SSQhs'
FILE_EXCEL_GOOGLE = 'ILT_School_bot'
WORK_SHEET_EXCEL_GOOGLE = 'list'
```

docker build -t tg-bot-ilt_school --no-cache .

docker run -d \
  --name ilt_school \
  --restart=always \
  --env-file .env \
  tg-bot-ilt_school

docker stop ilt_school
docker rm ilt_school 
