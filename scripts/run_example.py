from sorter.models.package import Package
from sorter.utils.encoder import CustomEncoder
import json

pkg = Package(width=100, height=200, length=50, mass=25)
print(json.dumps(pkg, cls=CustomEncoder, indent=2))
