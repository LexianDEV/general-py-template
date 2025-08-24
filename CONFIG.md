# Configuration System

This Python template includes a Laravel-inspired configuration system that allows you to manage application settings through Python files and settings overrides.

## Features

- **Multiple Config Files**: Organize your configuration into separate Python files (e.g., `app.py`)
- **Settings Overrides**: Use `config/settings.py` file or environment variables to override config values
- **Bundled Settings**: Settings are bundled with the application binary (no external .env files needed)
- **Dot Notation Access**: Access nested configuration using dot notation (e.g., `app.name`, `app.logging.level`)
- **Runtime Changes**: Modify configuration values at runtime for testing or dynamic behavior
- **Helper Functions**: Easy-to-use helper functions for common config operations

## Usage

### Basic Configuration Access

```python
import helpers

# Get configuration values using dot notation
app_name = helpers.get_config('app.name', 'Default App')
response_number = helpers.get_config('app.response_number', 42)
debug_mode = helpers.get_config('app.debug', False)

# Check if a configuration exists
if helpers.has_config('app.name'):
    print("App name is configured")

# Get all configuration for a file
all_app_config = helpers.get_all_config('app')
```

### Settings File Overrides

Settings take precedence over config files but can be overridden by environment variables. Use uppercase and underscores:

- `app.name` → `APP_NAME`
- `app.response_number` → `APP_RESPONSE_NUMBER`
- `app.logging.level` → `APP_LOGGING_LEVEL`

Example `config/settings.py` file:
```python
# Application Settings - these override config/app.py values
APP_NAME = "My Custom App"
APP_DEBUG = True
APP_RESPONSE_NUMBER = 100
APP_MESSAGE = "Hello from the bundled settings!"
```

### Environment Variable Overrides

Environment variables have the highest precedence and will override both config files and settings:

```bash
export APP_NAME="Production App"
export APP_DEBUG=false
```

**Precedence Order (highest to lowest):**
1. Environment variables
2. Settings file (`config/settings.py`)
3. Config files (`config/*.py`)

### Runtime Configuration Changes

```python
# Modify configuration at runtime (doesn't persist)
helpers.set_config('app.name', 'Runtime Modified Name')

# Reload configuration from files
helpers.reload_config()  # Reload all
helpers.reload_config('app')  # Reload specific file
```

## Configuration Files

### Creating New Config Files

1. Create a new Python file in the `config/` directory
2. Define configuration variables as module-level variables
3. Use dictionaries for nested configuration

Example `config/services.py`:
```python
# External service configurations
api_key = "your-api-key-here"

external_api = {
    "base_url": "https://api.example.com",
    "timeout": 30,
    "retry_attempts": 3
}

cache = {
    "enabled": True,
    "ttl": 3600
}
```

### Existing Config Files

- **`app.py`**: Application-wide settings (name, version, debug mode, response number, etc.)
- **`settings.py`**: Override settings bundled with the application

## Advanced Usage

### Direct Config Manager Access

```python
from config_manager import ConfigManager

# Create a custom config manager
config = ConfigManager(config_dir="custom_config", settings_file="custom_settings")

# Use the manager directly
value = config.get('custom.setting', 'default')
config.set('custom.setting', 'new_value')
```

### Environment Helper

```python
# Get environment variable with fallback to config
value = helpers.env('API_KEY', 'default-key')
value = helpers.env('app.name')  # Falls back to config if no env var
```

## Best Practices

1. **Organize by Feature**: Create separate config files for different aspects (database, mail, cache, etc.)
2. **Use Settings File**: For non-sensitive application-specific overrides that should be bundled
3. **Use Environment Variables**: For sensitive data and deployment-specific settings
4. **Provide Defaults**: Always provide sensible default values
5. **Document Settings**: Add comments to explain complex configuration options
6. **Validate Config**: Add validation for critical configuration values in your application startup

## Example: Full Configuration Workflow

```python
import helpers

# Application startup - validate critical config
if not helpers.has_config('app.name'):
    raise ValueError("App name must be configured")

# Get database connection details
db_config = helpers.get_all_config('database')
connection = db_config['connections'][db_config['default']]

# Use environment override for sensitive data
api_key = helpers.env('API_KEY')
if not api_key:
    raise ValueError("API_KEY environment variable required")

# Runtime configuration for testing
if helpers.get_config('app.env') == 'testing':
    helpers.set_config('app.debug', True)
    helpers.set_config('database.default', 'sqlite')
```

This configuration system provides the flexibility of Laravel's config system while maintaining Python's simplicity and power. Settings are now bundled with the application for easier distribution.