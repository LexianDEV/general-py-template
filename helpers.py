def time():
    from datetime import datetime as dt
    now = dt.now()
    return now.strftime("%I:%M %p")


# Configuration helper functions
from config_manager import config, config_set, config_reload, config_all, config_has


def get_config(key: str, default=None):
    """Get a configuration value using dot notation (e.g., 'app.name')."""
    return config(key, default)


def set_config(key: str, value):
    """Set a configuration value (runtime only)."""
    config_set(key, value)


def reload_config(config_name=None):
    """Reload configuration files."""
    config_reload(config_name)


def get_all_config(config_name: str):
    """Get all configuration values for a specific config file."""
    return config_all(config_name)


def has_config(key: str):
    """Check if a configuration key exists."""
    return config_has(key)


def env(key: str, default=None):
    """Get an environment variable or config value."""
    import os
    # Check environment variables first
    env_value = os.environ.get(key.upper())
    if env_value is not None:
        return env_value
    
    # Fall back to config if key contains dots
    if '.' in key:
        return get_config(key, default)
    
    return default
