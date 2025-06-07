import json
from sorter.enums.enums import DispatchStack
from sorter.models.package import Package

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, DispatchStack):
            return str(obj)
        if isinstance(obj, Package):
            return obj.to_dict()
        return super().default(obj)
