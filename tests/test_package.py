import unittest
from pydantic import ValidationError
from sorter.models.package import Package
from sorter.enums.enums import DispatchStack


class TestPackageDispatch(unittest.TestCase):
    def test_standard(self):
        p = Package(width=50, height=40, length=30, mass=10)
        self.assertEqual(p.dispatch_stack(), DispatchStack.STANDARD)

    def test_special_bulky(self):
        p = Package(width=200, height=100, length=60, mass=10)
        self.assertEqual(p.dispatch_stack(), DispatchStack.SPECIAL)

    def test_rejected(self):
        p = Package(width=200, height=200, length=200, mass=25)
        self.assertEqual(p.dispatch_stack(), DispatchStack.REJECTED)

    # Edge boundary tests
    def test_edge_volume_threshold(self):
        # Volume = 100 * 100 * 100 = 1,000,000 exactly
        p = Package(width=100, height=100, length=100, mass=10)
        self.assertTrue(p.is_bulky)
        self.assertEqual(p.dispatch_stack(), DispatchStack.SPECIAL)

    def test_edge_dimension_threshold(self):
        p = Package(width=150, height=50, length=50, mass=10)
        self.assertTrue(p.is_bulky)
        self.assertEqual(p.dispatch_stack(), DispatchStack.SPECIAL)

    def test_edge_mass_threshold(self):
        p = Package(width=50, height=50, length=50, mass=20)
        self.assertTrue(p.is_heavy)
        self.assertEqual(p.dispatch_stack(), DispatchStack.SPECIAL)

    def test_rejected_exact_threshold(self):
        # Exactly bulky and heavy at threshold
        p = Package(width=150, height=150, length=150, mass=20)
        self.assertTrue(p.is_bulky)
        self.assertTrue(p.is_heavy)
        self.assertEqual(p.dispatch_stack(), DispatchStack.REJECTED)

    # Validation tests for invalid inputs
    def test_invalid_zero_dimension(self):
        with self.assertRaises(ValidationError):
            Package(width=0, height=50, length=50, mass=10)

    def test_invalid_negative_mass(self):
        with self.assertRaises(ValidationError):
            Package(width=50, height=50, length=50, mass=-1)


if __name__ == "__main__":
    unittest.main()
