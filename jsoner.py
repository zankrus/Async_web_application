"""Файл для работы с JSON."""
import random
import re
from service import approve_cod , id_randomizer, address_creater, status_randomizer, weight_generator, create_time
from json_schema import json_schema


def json_messager() -> dict:
    """Тестовая функция-генерирует тестовые JSON, как валидный так и нет."""
    # random_event = random.randint(2, 4)
    # if random_event > 1:
    jeson_valid = {
        "id": id_randomizer(),
        "sender": address_creater(),
        "recipient": address_creater(),
        "status": status_randomizer(),
        "weight": weight_generator(),
        "creation_date": str(create_time()),
        "approve_code": approve_cod()
        }
    return jeson_valid


print(json_messager())



