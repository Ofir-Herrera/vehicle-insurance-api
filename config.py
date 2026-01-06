class Settings:
    """
    Configuration class for flexible change of business logic
    without changing the core code.
    """

    # Constants
    CURRENT_YEAR = 2026
    BASE_VALUE = 50000
    DEPRECIATION_PER_YEAR = 2000

    # API Metadata
    APP_TITLE = "Insait Vehicle Insurance Assignment"
    APP_VERSION = "1.0.0"


# Create a singleton instance of the settings
settings = Settings()