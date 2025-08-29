"""
Simple test for application functionality.
"""

import sys
import os

# Add the project root to the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules import AppModule, DisplayModule


def test_foundation():
    """Test that application foundation works properly."""
    print("Testing application foundation...")
    
    # Test display module methods
    display = DisplayModule()
    
    # These should run without error
    display.show_header()
    display.show_app_info()
    display.show_app_response()
    display.show_config_source()
    
    print("✓ All display methods work")
    
    # Test app module
    app = AppModule()
    app.initialize()
    app.cleanup()
    
    print("✓ App module lifecycle methods work")
    
    return True


def test_main_functionality():
    """Test the main app functionality."""
    print("Testing main app functionality...")
    
    app = AppModule()
    # This should produce the same output as before
    app.run()
    
    print("✓ Main functionality works")
    return True


def test_delayed_functionality():
    """Test the delayed display functionality."""
    print("Testing delayed display functionality...")
    
    app = AppModule()
    # Test the demo method with delays
    app.start_with_demo()
    
    print("✓ Delayed functionality works")
    return True


def run_tests():
    """Run all tests."""
    try:
        test_foundation()
        test_main_functionality()
        test_delayed_functionality()
        print("\n✅ All tests passed!")
        return True
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        return False


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)