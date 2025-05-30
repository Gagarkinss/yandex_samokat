# Алина Фидаева, 30а Venus — Финальный проект. Инженер по тестированию плюс
import pytest
import sender_stand_request
import data

def test_create_order_and_get_by_track():
    # Шаг 1: Создание заказа
    response_create = sender_stand_request.create_order(data.order_body)
    assert response_create.status_code == 201, (
        f"Ожидался код 201 (Order Created), но получен {response_create.status_code}. "
        f"Тело ответа: {response_create.text}"
    )
    
    # Шаг 2: Сохранение номера трека
    track_number = response_create.json()["track"]
    assert track_number is not None, "Трек-номер отсутствует в ответе сервера"
    
    # Шаг 3: Получение заказа по треку (позитивный сценарий)
    response_get = sender_stand_request.get_order_by_track(track_number)
    assert response_get.status_code == 200, (
        f"Ожидался код 200 (OK), но получен {response_get.status_code}. "
        f"Трек: {track_number}, Ответ сервера: {response_get.text}"
    )
