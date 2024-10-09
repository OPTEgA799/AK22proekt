import requests
import configuration
import data


# Создание заказа
def post_order(body):
    return requests.post(url=f"{configuration.URL_SERVICE}{configuration.CREATE_ORDER}",
                         json=body,
                         headers=data.headers)


# Получение заказа по номеру
def get_order(track_number):
    return requests.get(url=f"{configuration.URL_SERVICE}{configuration.GET_TRACK}{track_number}")

