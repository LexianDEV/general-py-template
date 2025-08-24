"""
Laravel-like configuration manager for Python applications.
Supports loading config files from the config directory and environment overrides.
"""

import os
import importlib.util
from typing import Any, Dict, Optional
from pathlib import Path


class ConfigManager:
    """Manages application configuration with support for multiple config files and environment overrides."""
    
    def __init__(self, config_dir: str = "config", env_file: str = ".env"):
        self.config_dir = Path(config_dir)
        self.env_file = Path(env_file)
        self._config_cache: Dict[str, Dict[str, Any]] = {}
        self._env_vars: Dict[str, str] = {}
        
        # Load environment variables from .env file
        self._load_env_file()
        
    def _load_env_file(self) -> None:
        """Load environment variables from .env file if it exists."""
        if self.env_file.exists():
            with open(self.env_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#') and '=' in line:
                        key, value = line.split('=', 1)
                        self._env_vars[key.strip()] = value.strip().strip('"').strip("'")
    
    def _load_config_file(self, config_name: str) -> Dict[str, Any]:
        """Load a specific config file."""
        config_file = self.config_dir / f"{config_name}.py"
        
        if not config_file.exists():
            return {}
            
        spec = importlib.util.spec_from_file_location(config_name, config_file)
        if spec is None or spec.loader is None:
            return {}
            
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Extract all non-private attributes as config values
        config_data = {}
        for attr_name in dir(module):
            if not attr_name.startswith('_'):
                config_data[attr_name] = getattr(module, attr_name)
                
        return config_data
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get a configuration value using dot notation (e.g., 'app.name' or 'database.host').
        Environment variables take precedence over config files.
        """
        # Check for environment variable override first
        env_key = key.upper().replace('.', '_')
        if env_key in self._env_vars:
            value = self._env_vars[env_key]
            # Convert string boolean values
            if value.lower() in ('true', 'false'):
                return value.lower() == 'true'
            return value
        if env_key in os.environ:
            value = os.environ[env_key]
            # Convert string boolean values
            if value.lower() in ('true', 'false'):
                return value.lower() == 'true'
            return value
            
        # Parse the key to get config file and setting
        if '.' not in key:
            return default
            
        config_name, setting_path = key.split('.', 1)
        
        # Load config file if not cached
        if config_name not in self._config_cache:
            self._config_cache[config_name] = self._load_config_file(config_name)
            
        config_data = self._config_cache[config_name]
        
        # Navigate through nested settings using dot notation
        current = config_data
        for part in setting_path.split('.'):
            if isinstance(current, dict) and part in current:
                current = current[part]
            else:
                return default
                
        return current
    
    def set(self, key: str, value: Any) -> None:
        """Set a configuration value in the cache (runtime only)."""
        if '.' not in key:
            return
            
        config_name, setting_path = key.split('.', 1)
        
        # Ensure config is loaded
        if config_name not in self._config_cache:
            self._config_cache[config_name] = self._load_config_file(config_name)
            
        # Navigate and set the value
        current = self._config_cache[config_name]
        parts = setting_path.split('.')
        
        for part in parts[:-1]:
            if part not in current or not isinstance(current[part], dict):
                current[part] = {}
            current = current[part]
            
        current[parts[-1]] = value
    
    def reload(self, config_name: Optional[str] = None) -> None:
        """Reload configuration files. If config_name is None, reload all."""
        if config_name:
            if config_name in self._config_cache:
                del self._config_cache[config_name]
        else:
            self._config_cache.clear()
            self._load_env_file()
    
    def all(self, config_name: str) -> Dict[str, Any]:
        """Get all configuration values for a specific config file."""
        if config_name not in self._config_cache:
            self._config_cache[config_name] = self._load_config_file(config_name)
        return self._config_cache[config_name].copy()
    
    def has(self, key: str) -> bool:
        """Check if a configuration key exists."""
        sentinel = object()
        try:
            result = self.get(key, sentinel)
            return result is not sentinel
        except:
            return False


# Global config manager instance
_config_manager = ConfigManager()


def config(key: str, default: Any = None) -> Any:
    """Get a configuration value."""
    return _config_manager.get(key, default)


def config_set(key: str, value: Any) -> None:
    """Set a configuration value."""
    _config_manager.set(key, value)


def config_reload(config_name: Optional[str] = None) -> None:
    """Reload configuration."""
    _config_manager.reload(config_name)


def config_all(config_name: str) -> Dict[str, Any]:
    """Get all configuration for a config file."""
    return _config_manager.all(config_name)


def config_has(key: str) -> bool:
    """Check if a configuration key exists."""
    return _config_manager.has(key)