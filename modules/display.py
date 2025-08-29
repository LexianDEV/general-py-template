"""
Display module for managing application output and presentation.
Handles all display-related functionality.
"""

import time
import helpers


class DisplayModule:
    """Handles application display and output functionality."""
    
    def __init__(self):
        """Initialize the display module."""
        pass
    
    def show_header(self):
        """Display the application header."""
        print("=== General Python Template ===")
        print(f"Current time: {helpers.time()}")
        print()
    
    def show_app_info(self):
        """Display application information."""
        # Get basic app configuration
        app_name = helpers.get_config('app.name', 'Unknown App')
        app_version = helpers.get_config('app.version', '1.0.0')
        app_env = helpers.get_config('app.env', 'unknown')
        app_debug = helpers.get_config('app.debug', False)
        
        print(f"App: {app_name} v{app_version}")
        print(f"Environment: {app_env} (Debug: {app_debug})")
        print()
    
    def show_app_response(self):
        """Display the application response section."""
        response_number = helpers.get_config('app.response_number', 0)
        message = helpers.get_config('app.message', 'Hello, World!')
        
        print("=== App Response ===")
        print(f"Message: {message}")
        print(f"Response Number: {response_number}")
        print()
    
    def show_config_source(self):
        """Display configuration source information."""
        response_number = helpers.get_config('app.response_number', 0)
        message = helpers.get_config('app.message', 'Hello, World!')
        
        print("=== Configuration Source ===")
        
        # Check response number source
        env_number = helpers.env('APP_RESPONSE_NUMBER')
        if env_number:
            print(f"Response number is overridden by environment variable: {env_number}")
        else:
            print(f"Response number is from config file: {response_number}")
        
        # Check message source
        env_message = helpers.env('APP_MESSAGE')
        if env_message:
            print(f"Message is overridden by environment variable: {env_message}")
        else:
            print(f"Message is from config file: {message}")
    
    def show_all(self):
        """Display all application information sections."""
        self.show_header()
        self.show_app_info()
        self.show_app_response()
        self.show_config_source()
    
    def show_with_delay(self, delay_seconds: float = 0.1):
        """
        Example of delayed functionality - show all sections with small delays.
        This demonstrates functionality with timing control.
        """
        self.show_header()
        time.sleep(delay_seconds)
        
        self.show_app_info()
        time.sleep(delay_seconds)
        
        self.show_app_response()
        time.sleep(delay_seconds)
        
        self.show_config_source()