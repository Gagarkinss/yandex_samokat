# Алина Фидаева, 30а Venus — Финальный проект. Инженер по тестированию плюс
import requests
from config import URL_SERVICE, CREATE_ORDER_PATH, GET_ORDER_PATH
from create_order_request import order_data

def test_order_flow():
    
    # 1. Создаем заказ
    create_url = f"{URL_SERVICE}{CREATE_ORDER_PATH}"
    response = requests.post(create_url, json=order_data)
    print(f"[1] Создание заказа — код: {response.status_code}")
    
    if response.status_code != 201:
        print(f"❌ Ошибка! Ожидался код 201, получен {response.status_code}")
        return False
    
    # 2. Получаем трек
    track = response.json()["track"]
    print(f"[2] Трек заказа: {track}")
    
    # 3. Получаем заказ по треку
    get_url = f"{URL_SERVICE}{GET_ORDER_PATH}?t={track}"
    response = requests.get(get_url)
    print(f"[3] Получение заказа — код: {response.status_code}")
    
    # 4. Проверяем результат
    if response.status_code == 200:
        print("✅ Тест пройден! Заказ создан и получен.")
        print(f"Данные заказа: {response.json()}")
        return True
    else:
        print(f"❌ Ошибка! Ожидался код 200, получен {response.status_code}")
        return False

if __name__ == "__main__":
    test_order_flow()
