from pydantic import BaseModel, Field
from sorter.enums.enums import DispatchStack

class Package(BaseModel):
    width: float = Field(..., gt=0)
    height: float = Field(..., gt=0)
    length: float = Field(..., gt=0)
    mass: float = Field(..., gt=0)

    BULKY_VOLUME_THRESHOLD: int = 1_000_000
    BULKY_DIMENSION_THRESHOLD: int = 150
    HEAVY_MASS_THRESHOLD: int = 20

    @property
    def volume(self) -> float:
        return self.width * self.height * self.length

    @property
    def is_bulky(self) -> bool:
        return (
            self.volume >= self.BULKY_VOLUME_THRESHOLD or
            max(self.width, self.height, self.length) >= self.BULKY_DIMENSION_THRESHOLD
        )

    @property
    def is_heavy(self) -> bool:
        return self.mass >= self.HEAVY_MASS_THRESHOLD

    def dispatch_stack(self) -> DispatchStack:
        return (
            DispatchStack.REJECTED if self.is_bulky and self.is_heavy
            else DispatchStack.SPECIAL if self.is_bulky or self.is_heavy
            else DispatchStack.STANDARD
        )

    def to_dict(self):
        return {
            "width": self.width,
            "height": self.height,
            "length": self.length,
            "mass": self.mass,
            "volume": self.volume,
            "is_bulky": self.is_bulky,
            "is_heavy": self.is_heavy,
            "dispatch_stack": str(self.dispatch_stack())
        }
