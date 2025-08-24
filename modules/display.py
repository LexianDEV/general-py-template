"""
Display module for managing application output and presentation.
Handles all display-related functionality with async support.
"""

import asyncio
import helpers


class DisplayModule:
    """Handles application display and output functionality."""
    
    def __init__(self):
        """Initialize the display module."""
        pass
    
    async def show_header(self):
        """Display the application header."""
        print("=== General Python Template ===")
        print(f"Current time: {helpers.time()}")
        print()
    
    async def show_app_info(self):
        """Display application information."""
        # Get basic app configuration
        app_name = helpers.get_config('app.name', 'Unknown App')
        app_version = helpers.get_config('app.version', '1.0.0')
        app_env = helpers.get_config('app.env', 'unknown')
        app_debug = helpers.get_config('app.debug', False)
        
        print(f"App: {app_name} v{app_version}")
        print(f"Environment: {app_env} (Debug: {app_debug})")
        print()
    
    async def show_app_response(self):
        """Display the application response section."""
        response_number = helpers.get_config('app.response_number', 0)
        message = helpers.get_config('app.message', 'Hello, World!')
        
        print("=== App Response ===")
        print(f"Message: {message}")
        print(f"Response Number: {response_number}")
        print()
    
    async def show_config_source(self):
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
    
    async def show_all(self):
        """Display all application information sections."""
        await self.show_header()
        await self.show_app_info()
        await self.show_app_response()
        await self.show_config_source()
    
    async def show_with_delay(self, delay_seconds: float = 0.1):
        """
        Example of async functionality - show all sections with small delays.
        This demonstrates the async foundation in action.
        """
        await self.show_header()
        await asyncio.sleep(delay_seconds)
        
        await self.show_app_info()
        await asyncio.sleep(delay_seconds)
        
        await self.show_app_response()
        await asyncio.sleep(delay_seconds)
        
        await self.show_config_source()