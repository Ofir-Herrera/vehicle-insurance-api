# Import core frameworks and project modules
from fastapi import FastAPI, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from models import VehicleInfoRequest, APIResponse, VehicleData
from database import vehicle_db
from config import settings
from logic import calculate_vehicle_value

# Initialize the FastAPI app using settings from config.py
app = FastAPI(title=settings.APP_TITLE, version=settings.APP_VERSION)

# CORS Configuration
# Essential for allowing the Insait platform to communicate with this API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/vehicle-info", response_model=APIResponse, tags=["Vehicle Lookup"])
def get_vehicle_info(
        request: VehicleInfoRequest,
        authorization: str = Header(None)
):
    """
    Main Endpoint: Receives a license plate and returns vehicle details.
    Includes a robust security check and debug logging.
    """

    # --- DEBUGGING: Check what we received in the terminal ---
    print(f"\n--- API CALL RECEIVED ---")
    print(f"Header received: {authorization}")

    # --- SECURITY LAYER: ROBUST TOKEN VALIDATION ---
    #Define our secret key in lowercase for easier matching
    SECRET_KEY = "mysecrettoken123"

    # Convert the header to string and lowercase to avoid any mismatch errors
    auth_string = str(authorization).lower() if authorization else ""

    if not authorization or SECRET_KEY not in auth_string:
        print(f"RESULT: Access Denied (401)")
        print(f"-------------------------\n")
        raise HTTPException(
            status_code=401,
            detail="Unauthorized access. Please provide a valid Bearer Token."
        )

    print(f"RESULT: Access Granted (200)")
    # -----------------------------------------------

    # 1. Database Lookup
    vehicle_raw = vehicle_db.get(request.license_plate)

    if not vehicle_raw:
        print(f"RESULT: Vehicle Not Found (404)")
        print(f"-------------------------\n")
        raise HTTPException(
            status_code=404,
            detail=f"Vehicle with license plate {request.license_plate} not found"
        )

    # 2. Business Logic: Calculate value
    estimated_value = calculate_vehicle_value(vehicle_raw["year"])

    # 3. Data Transformation
    vehicle_data = VehicleData(
        **vehicle_raw,
        estimated_value=estimated_value
    )

    print(f"RESULT: Success. Returning data for {vehicle_raw['model']}")
    print(f"-------------------------\n")

    return APIResponse(
        success=True,
        data=vehicle_data
    )