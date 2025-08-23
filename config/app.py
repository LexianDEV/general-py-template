"""
Application configuration settings.
"""

# Application name
name = "General Python Template"

# Application version
version = "1.0.0"

# Environment (development, testing, production)
env = "development"

# Debug mode
debug = True

# Default response number that the app returns
response_number = 42

# Message to display
message = "Hello from the General Python Template!"

# Logging configuration
logging = {
    "level": "INFO",
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "file": "logs/app.log"
}