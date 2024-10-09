import data
import sender_stand_request


# Конюшенко Андрей. Когорта 22. Финальный проект.
def test_create_check_order():
    # 1. Запрос на создание заказа.
    response_create = sender_stand_request.post_order(data.order_body)

    # 2. Сохранить номер трека заказа.
    track_number = response_create.json()["track"]

    # 3. Запрос на получения заказа по треку заказа.
    response_order = sender_stand_request.get_order(track_number)

    # 4. Проверить, что код ответа равен 200.
    assert response_order.status_code == 200
