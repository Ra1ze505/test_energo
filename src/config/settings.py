import os

PROJECT_NAME = "Test ENERGO"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

API_V1_STR = "/api/v1"

# Secret key
SECRET_KEY = os.environ.get("SECRET_KEY")

# CORS
BACKEND_CORS_ORIGINS = ['*']

# Colors
COLORS = {
    "red": int(os.environ.get("COLORS_RED", 10)),
    "green": int(os.environ.get("COLORS_GREEN", 20)),
    "blue": int(os.environ.get("COLORS_BLUE", 70)),
}