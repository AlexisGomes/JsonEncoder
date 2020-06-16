from decimal import Decimal
from pprint import pprint

import arrow
from JsonEncoder import json_encode, json_decode
from MyClass import MyClass

# Encode a dict
json_encode({
    "name": "Paul",
    "birthdate": arrow.get("1992-02-22").datetime,
    "decimal_number": Decimal(14.456),
    "float_number": 14.456,
    "int_number": 122
})

# Encode a custom object
my_obj = MyClass("value1", "value2")
json_encode(my_obj)

# Encode nested dicts
json_encode({
    "name": "Paul",
    "birthdate": arrow.get("1992-02-22").datetime,
    "decimal_number": Decimal(14.456),
    "float_number": 14.456,
    "int_number": 122,
    "my_dict": {
        "value_1": 1,
        "value_2": "2",
    },
    "list": [
    {
        "value_1": 1,
        "value_2": "2",
    },
    {
        "value_1": 1,
        "value_2": "2",
    },
    {
        "value_1": 1,
        "value_2": "2",
    }
    ]
})

# Decode a dict with various types
json_decode('{"name": "Paul", "birthdate": "1992-02-22T00:00:00+00:00", "float_number": 14.456, "int_number": 122}')

# Decode a dict, with nested dicts and list
json_decode('{"name": "Paul", "birthdate": "1992-02-22T00:00:00+00:00", "decimal_number": 14.46, "float_number": 14.456, "int_number": 122, "my_dict": {"value_1": 1, "value_2": "2"}, "list": [{"value_1": 1, "value_2": "2"}, {"value_1": 1, "value_2": "2"}, {"value_1": 1, "value_2": "2"}]}')

# Decode an object of MyClass
json_decode("{\"value1\": \"value1\", \"value2\": \"value2\"}")
