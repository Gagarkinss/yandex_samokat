import requests
from config import URL_SERVICE, CREATE_ORDER_PATH, GET_ORDER_PATH

def create_order(body): # Функция для создания заказа через POST-запрос
    return requests.post(URL_SERVICE + CREATE_ORDER_PATH, json=body)

def get_order_by_track(track): # Функция для получения данных заказа по трек-номеру
    return requests.get(URL_SERVICE + GET_ORDER_PATH, params={"t": track})
