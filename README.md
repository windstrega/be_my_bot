# Проект CatBot

CatBot - это бот для Telegram, который присылает пользователю котиков.

## Установка

1. Клонируйте репозиторий с github
2. Создайте виртуальное окружение
3. Установите зависимости `pip install -r requirements.txt`
4. Создайте файл `settings.py`
5. Впишите в settings.py переменные:
```
API_KEY = "API - ключ бота"
PROXY_URL = "Адрес прокси"
PROXY_USERNAME = "Пароль на прокси"
PROXY_PASSWORD = "python"
USER_EMOJI =[':smiling_imp:', ':triumph:', ':sunglasses:', ':thumbsup:']
```
6. Запустите бота командой `python bot.py`