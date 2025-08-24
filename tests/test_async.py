"""
Simple test for async functionality.
"""

import asyncio
import sys
import os

# Add the project root to the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules import AppModule, DisplayModule


async def test_async_foundation():
    """Test that async foundation works properly."""
    print("Testing async foundation...")
    
    # Test display module async methods
    display = DisplayModule()
    
    # These should run without error
    await display.show_header()
    await display.show_app_info()
    await display.show_app_response()
    await display.show_config_source()
    
    print("✓ All async display methods work")
    
    # Test app module
    app = AppModule()
    await app.initialize()
    await app.cleanup()
    
    print("✓ App module lifecycle methods work")
    
    return True


async def test_main_functionality():
    """Test the main app functionality through async interface."""
    print("Testing main app functionality through async...")
    
    app = AppModule()
    # This should produce the same output as before
    await app.run()
    
    print("✓ Main functionality works through async interface")
    return True


async def run_async_tests():
    """Run all async tests."""
    try:
        await test_async_foundation()
        await test_main_functionality()
        print("\n✅ All async tests passed!")
        return True
    except Exception as e:
        print(f"\n❌ Async test failed: {e}")
        return False


if __name__ == "__main__":
    success = asyncio.run(run_async_tests())
    sys.exit(0 if success else 1)