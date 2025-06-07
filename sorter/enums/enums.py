from enum import Enum

class DispatchStack(Enum):
    STANDARD = "Standard"
    SPECIAL = "Special"
    REJECTED = "Rejected"

    def __str__(self):
        return self.value
