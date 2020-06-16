"""
Custom json encoder & decoder classes
"""
import re
import json

from datetime import datetime
from decimal import Decimal, ROUND_UP

import arrow


# extend the json.JSONEncoder class
from MyClass import MyClass


class JSONEncoder(json.JSONEncoder):

    # overload method default
    def default(self, obj):

        # Match all the types you want to handle in your converter
        if isinstance(obj, datetime):
            return arrow.get(obj).isoformat()
        elif isinstance(obj, Decimal):
            return float(Decimal(obj).quantize(Decimal("0.01"), ROUND_UP))
        elif isinstance(obj, MyClass):
            return JSONEncoder().encode({
                "value1": obj.value_1,
                "value2": obj.value_2
            })

        # Call the default method for other types
        return json.JSONEncoder.default(self, obj)


class JSONDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, obj):

        # handle your custom classes
        if isinstance(obj, dict):
            if "value1" in obj and "value2" in obj:
                print(obj)
                return MyClass(obj.get("value_1"), obj.get("value_2"))

        # handling the resolution of nested objects
        if isinstance(obj, dict):
            for key in list(obj):
                obj[key] = self.object_hook(obj[key])

            return obj

        if isinstance(obj, list):
            for i in range(0, len(obj)):
                obj[i] = self.object_hook(obj[i])

            return obj

        # resolving simple strings objects
        # dates
        if isinstance(obj, str):
            obj = self._extract_date(obj)

        return obj

    @staticmethod
    def _extract_date(value):
        # iso format
        if re.search(
            r"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(\.[0-9]+)*\+[0-9]{2}:[0-9]{2}$",
            value,
        ):
            value = arrow.get(value).datetime
        return value


def json_encode(data):
    return JSONEncoder().encode(data)


def json_decode(string):
    return JSONDecoder().decode(string)
