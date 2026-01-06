from config import settings

# Business logic
def calculate_vehicle_value(year: int)->float:

    """
    Calculates the estimated market value based on vehicle age.
    Uses constants from config.py to ensure easy updates.
    """
    # Calculate vehicle age: (current year - manufacturing year)
    age = settings.CURRENT_YEAR - year
    # Calculate the value of the vehicle, a fixed amount is subtracted per year.
    value = settings.BASE_VALUE - (age*settings.DEPRECIATION_PER_YEAR)
    # Return the value, use maximum to avoid negative estimated market value.
    return float(max(0, value))