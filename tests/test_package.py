import unittest
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
        
    def test_heavy_not_bulky(self):
        p = Package(width=50, height=40, length=30, mass=25)
        self.assertEqual(p.dispatch_stack(), DispatchStack.SPECIAL)

if __name__ == "__main__":
    unittest.main()
