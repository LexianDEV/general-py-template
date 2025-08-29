"""
Main application module.
Coordinates application logic and flow.
"""

from .display import DisplayModule


class AppModule:
    """Main application module."""
    
    def __init__(self):
        """Initialize the application module."""
        self.display = DisplayModule()
    
    def run(self):
        """Run the main application logic."""
        # Run all display sections
        self.display.show_all()
    
    def initialize(self):
        """Initialize the application (setup)."""
        # Placeholder for any initialization
        # This could include database connections, API setup, etc.
        pass
    
    def cleanup(self):
        """Clean up resources (teardown)."""
        # Placeholder for any cleanup
        # This could include closing connections, saving state, etc.
        pass
    
    def start(self):
        """Start the application with full lifecycle management."""
        try:
            self.initialize()
            self.run()
        finally:
            self.cleanup()
    
    def start_with_demo(self):
        """
        Start the application with demonstration.
        Shows how the foundation can be utilized.
        """
        try:
            self.initialize()
            # Use the demo display method
            self.display.show_with_delay(0.05)
        finally:
            self.cleanup()