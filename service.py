"""Файл для хранения вспомогательных функций."""
import random
import string
from typing import Any

import jsonschema
from jsonschema import validate

from schema import SCHEMA


def status_randomizer() -> str:
    """Генерация случайного статуса посылки."""
    list_of_statuses = ['Обрабатывается', 'Выполняется ', 'Доставлено']
    status = random.choice(list_of_statuses)
    return status


def id_randomizer() -> str:
    """Генератор айди отправления"""
    def id_generator():
        count = 0
        while count < 1000:
            id = ''
            id += random.choice(string.ascii_lowercase)
            id += str(random.choice(string.digits))
            for i in range(random.randint(0, 3)):
                id += random.choice(string.ascii_lowercase) or str(random.choice(string.digits))
            count += 1
            yield id

    list_of_id = [x for x in id_generator()]
    return random.choice(list_of_id)


def input_validation(input_json: dict, schema: dict = SCHEMA) -> Any:
    """Валидатор входящего JSON."""
    print('Входящий JSON : ' + str(input_json))
    try:
        validate(input_json, schema)
        return input_json
    except jsonschema.exceptions.ValidationError:
        print('Json  провалил проверку валидации схемы')


