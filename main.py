# Import core frameworks and project modules
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import VehicleInfoRequest, APIResponse, VehicleData
from database import vehicle_db
from config import settings
from logic import calculate_vehicle_value

# Create app with the definitions from config
app = FastAPI(title=settings.APP_TITLE, version=settings.APP_VERSION)

# Cors configuration
# Required for integration with Insait and frontend clients.
# This allows the API to accept requests from different origins.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permits all origins for testing and Insait integration
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (POST, GET, etc.)
    allow_headers=["*"],  # Allows all headers
)


@app.post("/vehicle-info", response_model=APIResponse, tags=["Vehicle Lookup"])
def get_vehicle_info(request: VehicleInfoRequest):
    """
    Receives the license plate, searches for the vehicle in the DB,
    and returns all details including the calculated price.
    """

    # 1. Search in the "Database"
    vehicle_raw = vehicle_db.get(request.license_plate)

    # 2. Handle case where vehicle doesn't exist
    # If we didn't find anything, raise a clear error.
    if not vehicle_raw:
        raise HTTPException(
            status_code=404,
            detail=f"Vehicle with license plate {request.license_plate} not found"
        )

    # 3. Calculate value
    # The math logic is in 'logic.py' to keep this function clean and focused on the API part.
    estimated_value = calculate_vehicle_value(vehicle_raw["year"])

    # 4. Create the data object
    vehicle_data = VehicleData(
        **vehicle_raw,
        estimated_value=estimated_value
    )

    # 5. Send final response
    return APIResponse(success=True, data=vehicle_data)
