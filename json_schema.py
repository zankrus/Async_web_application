"""Файл для хранения JSON-схемы."""


json_schema = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The root schema",
    "description": "The root schema comprises the entire JSON document.",
    "default": {},
    "examples": [
        {
            "id": "A1",
            "sender": "Адоратского, 4",
            "recipient": "Пушкина, 4",
            "status": "Доставлено",
            "weight": 100,
            "creation_date": "2019-20-20 08:08",
            "approve_code": "AA444223232"
        }
    ],
    "required": [
        "id",
        "sender",
        "recipient",
        "status",
        "weight",
        "creation_date",
        "approve_code"
    ],
    "additionalProperties": True,
    "properties": {
        "id": {
            "$id": "#/properties/id",
            "type": "string",
            "title": "The id schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "A1"
            ]
        },
        "sender": {
            "$id": "#/properties/sender",
            "type": "string",
            "title": "The sender schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "Адоратского, 4"
            ]
        },
        "recipient": {
            "$id": "#/properties/recipient",
            "type": "string",
            "title": "The recipient schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "Пушкина, 4"
            ]
        },
        "status": {
            "$id": "#/properties/status",
            "type": "string",
            "title": "The status schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "Доставлено"
            ]
        },
        "weight": {
            "$id": "#/properties/weight",
            "type": "integer",
            "title": "The weight schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                100
            ]
        },
        "creation_date": {
            "$id": "#/properties/creation_date",
            "type": "string",
            "title": "The creation_date schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "2019-20-20 08:08"
            ]
        },
        "approve_code": {
            "$id": "#/properties/approve_code",
            "type": "string",
            "title": "The approve_code schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "AA444223232"
            ]
        }
    }
}