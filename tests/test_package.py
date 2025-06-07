import unittest
from pydantic import ValidationError
from sorter.models.package import Package
from sorter.enums.enums import DispatchStack
from sorter.services.dispatcher import sort


class TestPackageDispatch(unittest.TestCase):
    def test_standard(self):
        result = sort(50, 40, 30, 10)
        self.assertEqual(result, DispatchStack.STANDARD.value)

    def test_special_bulky(self):
        result = sort(200, 100, 60, 10)
        self.assertEqual(result, DispatchStack.SPECIAL.value)

    def test_rejected(self):
        result = sort(200, 200, 200, 25)
        self.assertEqual(result, DispatchStack.REJECTED.value)

    # Edge boundary tests
    def test_edge_volume_threshold(self):
        result = sort(100, 100, 100, 10)
        self.assertEqual(result, DispatchStack.SPECIAL.value)

    def test_edge_dimension_threshold(self):
        result = sort(150, 50, 50, 10)
        self.assertEqual(result, DispatchStack.SPECIAL.value)

    def test_edge_mass_threshold(self):
        result = sort(50, 50, 50, 20)
        self.assertEqual(result, DispatchStack.SPECIAL.value)

    def test_rejected_exact_threshold(self):
        result = sort(150, 150, 150, 20)
        self.assertEqual(result, DispatchStack.REJECTED.value)

    # Validation tests for invalid inputs
    def test_invalid_zero_dimension(self):
        with self.assertRaises(ValidationError):
            Package(width=0, height=50, length=50, mass=10)

    def test_invalid_negative_mass(self):
        with self.assertRaises(ValidationError):
            Package(width=50, height=50, length=50, mass=-1)


if __name__ == "__main__":
    unittest.main()
