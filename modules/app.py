"""
Main application module with async foundation.
Coordinates application logic and flow.
"""

import asyncio
from .display import DisplayModule


class AppModule:
    """Main application module with async support."""
    
    def __init__(self):
        """Initialize the application module."""
        self.display = DisplayModule()
    
    async def run(self):
        """Run the main application logic asynchronously."""
        # Run all display sections
        await self.display.show_all()
    
    async def initialize(self):
        """Initialize the application (async setup)."""
        # Placeholder for any async initialization
        # This could include database connections, API setup, etc.
        pass
    
    async def cleanup(self):
        """Clean up resources (async teardown)."""
        # Placeholder for any async cleanup
        # This could include closing connections, saving state, etc.
        pass
    
    async def start(self):
        """Start the application with full lifecycle management."""
        try:
            await self.initialize()
            await self.run()
        finally:
            await self.cleanup()
    
    async def start_with_async_demo(self):
        """
        Start the application with async demonstration.
        Shows how the async foundation can be utilized.
        """
        try:
            await self.initialize()
            # Use the async demo display method
            await self.display.show_with_delay(0.05)
        finally:
            await self.cleanup()