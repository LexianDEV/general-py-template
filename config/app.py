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

# Application URL
url = "http://localhost:8000"

# Timezone
timezone = "UTC"

# Locale settings
locale = {
    "default": "en",
    "fallback": "en",
    "supported": ["en", "es", "fr"]
}

# Logging configuration
logging = {
    "level": "INFO",
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "file": "logs/app.log"
}