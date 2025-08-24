"""
Simple tests for the config functionality.
"""

import os
import sys
import tempfile
import shutil
from pathlib import Path

# Add the project root to the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config_manager import ConfigManager


def test_config_loading():
    """Test basic config file loading."""
    print("Testing config file loading...")
    
    # Create a temporary config directory
    with tempfile.TemporaryDirectory() as temp_dir:
        config_dir = Path(temp_dir) / "config"
        config_dir.mkdir()
        
        # Create a test config file
        test_config = config_dir / "test.py"
        test_config.write_text("""
name = "Test App"
version = "1.0.0"
settings = {
    "debug": True,
    "host": "localhost"
}
""")
        
        # Test config manager
        manager = ConfigManager(config_dir=str(config_dir))
        
        # Test basic config loading
        assert manager.get('test.name') == "Test App"
        assert manager.get('test.version') == "1.0.0"
        assert manager.get('test.settings.debug') == True
        assert manager.get('test.settings.host') == "localhost"
        assert manager.get('test.nonexistent', 'default') == 'default'
        
        print("✓ Config file loading works")


def test_settings_overrides():
    """Test settings file overrides."""
    print("Testing settings overrides...")
    
    with tempfile.TemporaryDirectory() as temp_dir:
        config_dir = Path(temp_dir) / "config"
        config_dir.mkdir()
        
        # Create a test config file
        test_config = config_dir / "app.py"
        test_config.write_text("""
name = "Original App"
debug = False
""")
        
        # Create settings file
        settings_file = config_dir / "settings.py"
        settings_file.write_text("""
APP_NAME = "Override App"
APP_DEBUG = True
""")
        
        # Test config manager
        manager = ConfigManager(config_dir=str(config_dir), settings_file="settings")
        
        # Test settings overrides
        assert manager.get('app.name') == "Override App"
        assert manager.get('app.debug') == True
        
        print("✓ Settings overrides work")


def test_runtime_config_changes():
    """Test runtime configuration changes."""
    print("Testing runtime config changes...")
    
    with tempfile.TemporaryDirectory() as temp_dir:
        config_dir = Path(temp_dir) / "config"
        config_dir.mkdir()
        
        # Create a test config file
        test_config = config_dir / "app.py"
        test_config.write_text("""
name = "Original App"
""")
        
        # Test config manager with no settings file
        manager = ConfigManager(config_dir=str(config_dir), settings_file="nonexistent")
        
        # Test runtime changes
        original_name = manager.get('app.name')
        assert original_name == "Original App", f"Expected 'Original App', got '{original_name}'"
        manager.set('app.name', "Modified App")
        modified_name = manager.get('app.name')
        assert modified_name == "Modified App", f"Expected 'Modified App', got '{modified_name}'"
        
        # Test has method
        assert manager.has('app.name') == True
        assert manager.has('app.nonexistent') == False
        
        print("✓ Runtime config changes work")


def test_helpers_integration():
    """Test helper functions."""
    print("Testing helper functions...")
    
    import helpers
    
    # Test basic helper functions (these use the actual config files)
    app_name = helpers.get_config('app.name', 'default')
    assert app_name is not None
    
    # Test has_config
    assert helpers.has_config('app.name') == True
    assert helpers.has_config('nonexistent.key') == False
    
    print("✓ Helper functions work")


def run_tests():
    """Run all tests."""
    print("Running config system tests...\n")
    
    try:
        test_config_loading()
        test_settings_overrides()
        test_runtime_config_changes()
        test_helpers_integration()
        
        print("\n✅ All tests passed!")
        return True
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)