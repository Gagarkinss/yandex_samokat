# Автотест для проверки получения данных о заказе по его треку (Яндекс Самокат)

## Задача
Клиент создает заказ.
Проверяется, что по треку заказа можно получить данные о заказе.

## Шаги автотеста:
Выполнить запрос на создание заказа.
Сохранить номер трека заказа.
Выполнить запрос на получения заказа по треку заказа.
Проверить, что код ответа равен 200.

## Тест проверяет
Создание заказа (POST /api/v1/orders)
Получение заказа по треку (GET /api/v1/orders/track)
Код ответа 200 при успешном запросе

## Структура проекта 
| test_order.py      # Основной тест
| sender_stand_request.py  # Функции-запросы
| data.py           # Тестовые данные
| config.py         # Настройки API
| README.md         # Инструкция

## Используемые технологии
pytest - тест-раннер
requests - работа с HTTP-запросами
venv - управление виртуальным окружением

## Команды
pip install pytest
pip install requests
pytest --version
