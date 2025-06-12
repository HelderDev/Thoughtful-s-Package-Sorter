from sorter.models.package import Package
from sorter.enums.enums import DispatchStack
from sorter.services.csvReader import read_csv_file


def sort(width: float, height: float, length: float, mass: float) -> DispatchStack:
    """Grab the package and check which category it belongs to (REJECTED, SPECIAL or STANDARD)"""
    pkg = Package(width=width, height=height, length=length, mass=mass)
    if pkg.is_bulky and pkg.is_heavy:
        return DispatchStack.REJECTED
    if pkg.is_bulky or pkg.is_heavy:
        return DispatchStack.SPECIAL
    return DispatchStack.STANDARD


def calculateStatistics(file_path):
    data = read_csv_file(file_path)
    report = analyze_packages_from_data(data)
    print(report)

def analyze_packages_from_data(data):
    stats = {
        "STANDARD": [],
        "SPECIAL": [],
        "REJECTED": [],
    }

    total_packages = 0

    for row in data:
        total_packages += 1
        try:
            if row[0] <= 0 or row[1] <= 0 or row[2] <= 0 or row[3] <= 0:
                continue
            
            width = float(row[0]) if row[0] is not None else 0.0
            height = float(row[1]) if row[1] is not None else 0.0
            length = float(row[2]) if row[2] is not None else 0.0
            mass = float(row[3]) if row[3] is not None else 0.0
        except (ValueError, IndexError):
            continue  # Skip malformed rows

        volume = width * height * length
        stack = sort(width, height, length, mass)

        stats[stack.name].append({"mass": mass, "volume": volume})
        

    result = {"total_packages": total_packages, "stacks": {}}

    for stack, packages in stats.items():
        count = len(packages)
        mass_values = [p["mass"] for p in packages]
        volume_values = [p["volume"] for p in packages]

        result["stacks"][stack] = {
            "count": count,
            "percentage": (count / total_packages * 100) if total_packages else 0,
            "mass": {
                "avg": sum(mass_values) / count if count else 0,
                "min": min(mass_values) if mass_values else 0,
                "max": max(mass_values) if mass_values else 0,
            },
            "volume": {
                "avg": sum(volume_values) / count if count else 0,
                "min": min(volume_values) if volume_values else 0,
                "max": max(volume_values) if volume_values else 0,
            },
        }

    return result
