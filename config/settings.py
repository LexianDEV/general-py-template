"""
Application-wide settings and overrides.
This file contains environment-specific settings that can override config values.
Unlike traditional .env files, this is bundled with the application.
"""

# Application Settings - these override config/app.py values
APP_NAME = "My Custom App"
APP_ENV = "development"
APP_DEBUG = True
APP_RESPONSE_NUMBER = 100
APP_MESSAGE = "Hello from the bundled settings!"

# Logging Settings
APP_LOGGING_LEVEL = "DEBUG"