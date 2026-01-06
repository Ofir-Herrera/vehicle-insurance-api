import re
from pydantic import BaseModel, Field, field_validator
from typing import Optional

# --- Request Model ---
class VehicleInfoRequest(BaseModel):
    '''
    Filter information that enters. Make sure that license_plate written correctly.
    Defines the expected input structure for the vehicle lookup endpoint.
    Using Pydantic ensures validation before the data reaches our logic.
    '''
    license_plate: str = Field(..., description='Vehicle license plate', example='12-345-67')

    @field_validator('license_plate')
    def validate_license_plate_format(cls, value):
        """
        Validates that the license plate follows the specific pattern: 2 digits - 3 digits - 2 digits.
        Example: 12-345-67
        """
        # Define the regex pattern for the format XX-XXX-XX
        pattern = r"^\d{2}-\d{3}-\d{2}$"

        # Check if the input value matches the pattern
        if not re.match(pattern, value):
            raise ValueError('Invalid format. License plate must be XX-XXX-XX (e.g., 12-345-67)')

        return value

# -- Internal Data Model ---
class VehicleData(BaseModel):
    """
        Represents the actual vehicle data structure.
        This is nested inside the API response.
    """
    license_plate: str
    manufacturer: str
    model: str
    year: int
    color: str
    estimated_value: Optional[float] = None

# --- Response Model ---
class APIResponse(BaseModel):
    """
    Standardized API Response wrapper as required by the assignment specs.
    Structure: { "success": true, "data": { ... } }
    """
    success: bool
    error: Optional[str] = None
    data: Optional[VehicleData] = None