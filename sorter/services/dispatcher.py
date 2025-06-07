from sorter.models.package import Package


def sort(width: float, height: float, length: float, mass: float) -> str:
    pkg = Package(width=width, height=height, length=length, mass=mass)
    if pkg.is_bulky and pkg.is_heavy:
        return "Rejected"
    if pkg.is_bulky or pkg.is_heavy:
        return "Special"
    return "Standard"
        