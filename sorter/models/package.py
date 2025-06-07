from pydantic import BaseModel, Field


class Package(BaseModel):
    width: float = Field(..., gt=0)
    height: float = Field(..., gt=0)
    length: float = Field(..., gt=0)
    mass: float = Field(..., gt=0)

    BULKY_VOLUME_THRESHOLD: int = 1_000_000  # 1,000,000 cm³
    BULKY_DIMENSION_THRESHOLD: int = 150  # 150 cm
    HEAVY_MASS_THRESHOLD: int = 20  # 20 kg

    @property
    def volume(self) -> float:
        """Calculate the volume of the package (width * height * length)"""
        return self.width * self.height * self.length

    @property
    def is_bulky(self) -> bool:
        """Check if the package is bulky based on the BULKY_VOLUME_THRESHOLD and BULKY_DIMENSION_THRESHOLD,
        A package is bulky if its volume (Width x Height x Length) is greater than
        or equal to 1,000,000 cm³ or when one of its dimensions is greater or equal to 150 cm.
        """
        return (
            self.volume >= self.BULKY_VOLUME_THRESHOLD
            or max(self.width, self.height, self.length)
            >= self.BULKY_DIMENSION_THRESHOLD
        )

    @property
    def is_heavy(self) -> bool:
        """Check if the package is heavy based on the HEAVY_MASS_THRESHOLD,
        A package is heavy when its mass is greater or equal to 20 kg."""
        return self.mass >= self.HEAVY_MASS_THRESHOLD


