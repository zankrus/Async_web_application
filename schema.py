SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The root schema",
    "description": "The root schema comprises the entire JSON document.",
    "default": {},
    "examples": [
        {
            "id": "string",
            "status": "В доставке"
        }
    ],
    "required": [
        "id",
        "status"
    ],
    "additionalProperties": True,
    "properties": {
        "id": {
            "$id": "#/properties/id",
            "type": "string",
            "pattern": r"^[a-z0-9]{2,5}$",
            "title": "The id schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "string"
            ]
        },
        "status": {
            "$id": "#/properties/status",
            "type": "string",
            "pattern": r"(?i)(\W|^)(Доставлено|Выполняется|Обрабатывается)(\W|$)",
            "title": "The status schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "В доставке"
            ]
        }
    }
}