from decimal import Decimal
from pprint import pprint

import arrow
from JsonEncoder import json_encode, json_decode
from MyClass import MyClass

# Encode a dict
my_dict = {
    "name": "Paul",
    "birthdate": arrow.get("1992-02-22").datetime,
    "decimal_number": Decimal(14.456),
    "float_number": 14.456,
    "int_number": 122
}

json_encode(my_dict)
# '{"name": "Paul", "birthdate": "1992-02-22T00:00:00+00:00", "float_number": 14.456, "int_number": 122}'

# Encode a custom object
my_obj = MyClass("value1", "value2")
json_encode(my_obj)
# "{\"value1\": \"value1\", \"value2\": \"value2\"}"

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

# Decode a string
json_decode('{"name": "Paul", "birthdate": "1992-02-22T00:00:00+00:00", "float_number": 14.456, "int_number": 122}')


json_decode('{"name": "Paul", "birthdate": "1992-02-22T00:00:00+00:00", "decimal_number": 14.46, "float_number": 14.456, "int_number": 122, "my_dict": {"value_1": 1, "value_2": "2"}, "list": [{"value_1": 1, "value_2": "2"}, {"value_1": 1, "value_2": "2"}, {"value_1": 1, "value_2": "2"}]}')

res = json_decode("{\"value1\": \"value1\", \"value2\": \"value2\"}")
pprint(res)