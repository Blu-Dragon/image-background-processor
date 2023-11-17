import os
from dotenv import load_dotenv

load_dotenv()

# Application level
APP_SECRET_KEY = os.environ.get("APP_SECRET_KEY")

# External API
X_RAPID_API_KEY = os.environ.get("X_RAPID_API_KEY")
X_RAPID_API_HOST = os.environ.get("X_RAPID_API_HOST")

# Message types
MESSAGE_TYPE_SUCCESS = "success"
MESSAGE_TYPE_WARNING = "warning"
MESSAGE_TYPE_DANGER = "danger"
