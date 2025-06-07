from sorter.models.package import Package
from sorter.enums.enums import DispatchStack


def sort(width: float, height: float, length: float, mass: float) -> DispatchStack:
    """Grab the package and check which category it belongs to (REJECTED, SPECIAL or STANDARD)"""
    pkg = Package(width=width, height=height, length=length, mass=mass)
    if pkg.is_bulky and pkg.is_heavy:
        return DispatchStack.REJECTED
    if pkg.is_bulky or pkg.is_heavy:
        return DispatchStack.SPECIAL
    return DispatchStack.STANDARD
        